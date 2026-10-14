"""Small HTTP client for the FS Quiz API v2 and its image and document hosts.

Responses are cached on disk and requests are spaced out, so repeated local runs
do not hammer a free community service.
"""

import hashlib
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API_BASE_URL = "https://api.fs-quiz.eu/2/"
USER_AGENT = "fs-quiz-coach-import (+https://github.com/tudasha/Quizz-Workflow)"


class NotFound(Exception):
    pass


class FsQuizClient:
    def __init__(self, cache_dir=None, cache_max_age_s=24 * 3600, delay_s=0.2, retries=3, timeout_s=60):
        self.cache_dir = Path(cache_dir) if cache_dir else None
        self.cache_max_age_s = cache_max_age_s
        self.delay_s = delay_s
        self.retries = retries
        self.timeout_s = timeout_s
        self._last_request_at = 0.0

    def get_json(self, route, params=None):
        """GET an API route ("quiz/12"); raises NotFound for the API's 404."""
        url = API_BASE_URL + route.lstrip("/")
        if params:
            url += "?" + urllib.parse.urlencode(params)
        cached = self._read_cache(url)
        if cached is not None:
            return json.loads(cached)
        body = self._fetch(url)
        data = json.loads(body)
        # The API answers "not found" with a JSON status block, sometimes with HTTP 200.
        if isinstance(data, dict) and isinstance(data.get("status"), dict) and data["status"].get("code") == 404:
            raise NotFound(url)
        self._write_cache(url, body)
        return data

    def get_all_pages(self, route, list_key, params=None, page_size=25):
        """Collect every page of a list route that pages with start_id (1, 26, 51, ...)."""
        items = []
        start_id = 1
        while True:
            page_params = dict(params or {}, start_id=start_id)
            try:
                page = self.get_json(route, page_params).get(list_key) or []
            except NotFound:
                break
            items += page
            if len(page) < page_size:
                break
            start_id += page_size
        return items

    def download(self, url, target_path):
        """Save a file (image, PDF) unless it is already on disk. Returns True if downloaded."""
        target_path = Path(target_path)
        if target_path.exists() and target_path.stat().st_size > 0:
            return False
        body = self._fetch(url)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        temporary_path = target_path.with_name(target_path.name + ".part")
        temporary_path.write_bytes(body)
        temporary_path.replace(target_path)
        return True

    def _fetch(self, url):
        last_error = None
        for attempt in range(self.retries):
            self._wait_turn()
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            try:
                with urllib.request.urlopen(request, timeout=self.timeout_s) as response:
                    return response.read()
            except urllib.error.HTTPError as error:
                if error.code == 404:
                    body = error.read()
                    # The API puts its 404 in a JSON body; files just 404.
                    if url.startswith(API_BASE_URL):
                        return body
                    raise NotFound(url) from error
                last_error = error
                if error.code < 500 and error.code != 429:
                    raise
            except (urllib.error.URLError, TimeoutError) as error:
                last_error = error
            time.sleep(2 ** attempt)
        raise last_error

    def _wait_turn(self):
        wait_s = self._last_request_at + self.delay_s - time.monotonic()
        if wait_s > 0:
            time.sleep(wait_s)
        self._last_request_at = time.monotonic()

    def _cache_path(self, url):
        return self.cache_dir / (hashlib.sha256(url.encode()).hexdigest() + ".json")

    def _read_cache(self, url):
        if not self.cache_dir:
            return None
        path = self._cache_path(url)
        if not path.exists() or time.time() - path.stat().st_mtime > self.cache_max_age_s:
            return None
        return path.read_bytes()

    def _write_cache(self, url, body):
        if not self.cache_dir:
            return
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self._cache_path(url).write_bytes(body)
