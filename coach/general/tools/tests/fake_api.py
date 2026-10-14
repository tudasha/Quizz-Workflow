"""In-memory stand-in for FsQuizClient, built from the examples in the FS Quiz API spec."""

from fsquiz.client import NotFound


class FakeClient:
    def __init__(self, routes, files=None):
        self.routes = routes
        self.files = files or {}
        self.downloaded = []

    def get_json(self, route, params=None):
        key = route
        if params:
            key += "?" + "&".join(name + "=" + str(value) for name, value in sorted(params.items()))
        if key not in self.routes:
            raise NotFound(key)
        return self.routes[key]

    def get_all_pages(self, route, list_key, params=None, page_size=25):
        try:
            return self.get_json(route, dict(params or {}, start_id=1)).get(list_key) or []
        except NotFound:
            return []

    def download(self, url, target_path):
        if url not in self.files:
            raise NotFound(url)
        if target_path.exists():
            return False
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_bytes(self.files[url])
        self.downloaded.append(url)
        return True


FSN = {"id": 1, "short_name": "FSN", "event_name": "Formula Student Netherlands", "country": "Netherlands", "website": "https://formula-student.nl/"}
FSCH = {"id": 2, "short_name": "FSCH", "event_name": "Formula Student Switzerland", "country": "Switzerland", "website": "https://formulastudent.ch/"}


def event_all():
    return {"events": [
        dict(FSN, quizzes=[
            {"quiz_id": 1, "event_id": 1, "year": 2019, "class": "ev", "information": None, "date": "2019-02-01", "status": "complete"},
            {"quiz_id": 7, "event_id": 1, "year": 2020, "class": "cv", "information": None, "date": "2020-02-01", "status": "unpublished"},
        ]),
        dict(FSCH, quizzes=[
            {"quiz_id": 1, "event_id": 2, "year": 2019, "class": "ev", "information": None, "date": "2019-02-01", "status": "complete"},
        ]),
    ]}


def quiz_1():
    return {
        "quiz_id": 1, "year": "2019", "class": "ev", "information": None, "date": "2019-02-01", "status": "complete",
        "event": [FSN, FSCH],
        "questions": [
            {
                "position_index": 1, "question_id": "1",
                "text": "What will Young's Modulus be for a 20 mm square bar and with a length of 600mm when it lengthens by 0.5 mm under a load of 45 kN?    ",
                "time": None, "type": "single-choice",
                "answers": [
                    {"answer_id": 2, "question_id": 1, "answer_text": "180 GPa", "is_correct": False},
                    {"answer_id": 1, "question_id": 1, "answer_text": "135 GPa", "is_correct": True},
                ],
                "images": [{"img_id": 1, "path": "12_1.jpg"}],
                "solution": [{"solution_id": 4, "question_id": 1, "text": "E = F L / (A dL)<br>= 135 GPa", "images": [{"img_id": 9, "path": "s_1.png"}]}],
            },
            {
                "position_index": 2, "question_id": "2",
                "text": "Energy of the accumulator in kWh if 1 &lt; x?<br><img src=\"https://img.fs-quiz.eu/testquiz/abc.jpg\">",
                "time": 300, "type": "input",
                "answers": [{"answer_id": 6, "question_id": 2, "answer_text": "6.48", "is_correct": True}],
                "images": [],
                "solution": [],
            },
        ],
        "documents": [], "last_qualifier": None,
    }


def question_all():
    return {"questions": [
        {"question_id": "1", "text": "...", "type": "single-choice", "year": "2019", "event_id": "1, 2", "class": "ev",
         "mechanical": "1", "electronic": "0", "scoring": "0", "static": "0", "dynamic": "0", "rule": "0", "math": "1"},
    ]}


def routes():
    return {"event/all": event_all(), "quiz/1": quiz_1(), "question/all": question_all()}


def files():
    return {
        "https://img.fs-quiz.eu/12_1.jpg": b"jpg",
        "https://img.fs-quiz.eu/s_1.png": b"png",
        "https://img.fs-quiz.eu/testquiz/abc.jpg": b"inline",
    }


CONFIG = {
    "current_year": 2026,
    "quiz_statuses": ["complete"],
    "events": [],
    "skip_events": [],
    "folder_names": {},
    "document_types": {"general": ["Rulebook"], "competition": ["Handbook", "Additional Rules"]},
    "general_rulebook_pattern": "^FS[-_ ]?Rules",
    "zip_split_above_mb": 25,
}
