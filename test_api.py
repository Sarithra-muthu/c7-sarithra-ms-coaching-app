import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

FAKE_FEEDBACK = (
    "MARKS: 40 / 50\n\n"
    "DONE WELL:\nGood arithmetic.\n\n"
    "WENT WRONG:\nMinor errors.\n\n"
    "STEPS TO IMPROVE:\n1. Check your working."
)


class TestHealth(unittest.TestCase):
    def test_returns_200_and_status_ok(self):
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})


class TestAnalyse(unittest.TestCase):
    @patch("api.analyse_work", return_value=FAKE_FEEDBACK)
    def test_valid_subject_returns_200_with_fields(self, _mock):
        response = client.post(
            "/analyse",
            json={"subject": "Maths", "work_content": "1 + 1 = 2"},
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("subject", data)
        self.assertIn("feedback", data)
        self.assertEqual(data["subject"], "Maths")
        self.assertEqual(data["feedback"], FAKE_FEEDBACK)

    @patch("api.analyse_work", side_effect=ValueError(
        "Invalid subject 'Foo'. Must be one of: Maths, Comprehension, Creative Writing"
    ))
    def test_invalid_subject_returns_400(self, _mock):
        response = client.post(
            "/analyse",
            json={"subject": "Foo", "work_content": "some work"},
        )
        self.assertEqual(response.status_code, 400)

    def test_empty_work_content_returns_422(self):
        response = client.post(
            "/analyse",
            json={"subject": "Maths", "work_content": ""},
        )
        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()
