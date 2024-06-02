import unittest
import requests

class TestFlaskAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:5000"

    def test_home_route(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Welcome to the Flask API!")

    def test_data_route(self):
        response = requests.get(self.base_url + "/data")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json())

    def test_status_route(self):
        response = requests.get(self.base_url + "/status")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")

    def test_add_user_route(self):
        data = {
            "username": "test_user",
            "name": "Test User",
            "age": 30,
            "city": "Test City"
        }
        response = requests.post(self.base_url + "/add_user", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["user"]["username"], "test_user")

        # Attempt to add a user with duplicate username
        response = requests.post(self.base_url + "/add_user", json=data)
        self.assertEqual(response.status_code, 409)

    def test_get_user_route(self):
        response = requests.get(self.base_url + "/users/test_user")
        self.assertEqual(response.status_code, 404)  # User not found initially

        # Add a user and then fetch
        data = {
            "username": "test_user",
            "name": "Test User",
            "age": 30,
            "city": "Test City"
        }
        requests.post(self.base_url + "/add_user", json=data)
        response = requests.get(self.base_url + "/users/test_user")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["username"], "test_user")

if __name__ == "__main__":
    unittest.main()
