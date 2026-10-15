
import unittest
from docker.backend.app import app


class BackendTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_endpoint(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_api_endpoint(self):
        response = self.client.get("/api")
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Hello from Flask API",
            response.data
        )


if __name__ == "__main__":
    unittest.main()
