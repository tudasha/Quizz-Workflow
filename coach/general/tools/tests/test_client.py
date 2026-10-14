"""The real HTTP client against a local server that answers like the FS Quiz API."""

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

import pytest

from fsquiz import client as client_module
from fsquiz.client import FsQuizClient, NotFound

DOCUMENTS = [{"doc_id": number, "path": str(number) + ".pdf"} for number in range(1, 31)]


class FakeApiHandler(BaseHTTPRequestHandler):
    request_count = 0

    def do_GET(self):
        FakeApiHandler.request_count += 1
        url = urlparse(self.path)
        query = parse_qs(url.query)
        if url.path == "/2/event/all":
            self.send_json(200, {"events": [{"id": 1, "short_name": "FSN"}]})
        elif url.path == "/2/document":
            start = int(query["start_id"][0]) - 1
            page = DOCUMENTS[start:start + 25]
            if page:
                self.send_json(200, {"documents": page})
            else:
                self.send_json(404, {"status": {"code": 404, "massage": "Content not found"}})
        elif url.path == "/img/12_1.jpg":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"jpg")
        else:
            self.send_json(404, {"status": {"code": 404, "massage": "Content not found"}})

    def send_json(self, status, data):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


@pytest.fixture
def server_url(monkeypatch):
    server = ThreadingHTTPServer(("127.0.0.1", 0), FakeApiHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    url = "http://127.0.0.1:" + str(server.server_address[1])
    monkeypatch.setattr(client_module, "API_BASE_URL", url + "/2/")
    # The proxy settings of the machine must not catch requests to the local server.
    monkeypatch.setenv("NO_PROXY", "127.0.0.1")
    monkeypatch.setenv("no_proxy", "127.0.0.1")
    FakeApiHandler.request_count = 0
    yield url
    server.shutdown()


def test_get_json_and_not_found(server_url):
    client = FsQuizClient(delay_s=0)
    assert client.get_json("event/all")["events"][0]["short_name"] == "FSN"
    with pytest.raises(NotFound):
        client.get_json("quiz/999")


def test_get_all_pages_follows_start_id(server_url):
    client = FsQuizClient(delay_s=0)
    documents = client.get_all_pages("document", "documents", {"year": 2026})
    assert [document["doc_id"] for document in documents] == list(range(1, 31))


def test_cache_spares_the_api(server_url, tmp_path):
    client = FsQuizClient(cache_dir=tmp_path, delay_s=0)
    client.get_json("event/all")
    client.get_json("event/all")
    assert FakeApiHandler.request_count == 1


def test_download_saves_once_and_404_raises(server_url, tmp_path):
    client = FsQuizClient(delay_s=0)
    target = tmp_path / "images" / "12_1.jpg"
    assert client.download(server_url + "/img/12_1.jpg", target) is True
    assert target.read_bytes() == b"jpg"
    assert client.download(server_url + "/img/12_1.jpg", target) is False
    with pytest.raises(NotFound):
        client.download(server_url + "/img/gone.jpg", tmp_path / "gone.jpg")
