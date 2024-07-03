import unittest
from fastapi.testclient import TestClient
from main import app

class TestAirQualityAPI(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)
        self.city = "barcelona"  # Ciudad para la prueba
        self.token = "636874ca4a5ae201663d1649e8f658c11a442b83"  # Token de API para la prueba

    def test_get_air_quality(self):
        response = self.client.get(f"/feed/{self.city}?token={self.token}")
        print("Response status code:", response.status_code)
        print("Response content:", response.content)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("status", data)
        self.assertIn("data", data)

if __name__ == "__main__":
    unittest.main()
