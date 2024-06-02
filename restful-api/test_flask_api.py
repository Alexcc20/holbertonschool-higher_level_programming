import requests
import json

def test_flask_api():
    base_url = "http://localhost:5000"

    # Test the root endpoint
    response = requests.get(base_url)
    print(f"GET /: {response.status_code} - {response.text}")

    # Test the /data endpoint
    response = requests.get(f"{base_url}/data")
    print(f"GET /data: {response.status_code} - {response.json()}")

    # Test the /status endpoint
    response = requests.get(f"{base_url}/status")
    print(f"GET /status: {response.status_code} - {response.text}")

    # Test the /users/<username> endpoint
    response = requests.get(f"{base_url}/users/jane")
    print(f"GET /users/jane: {response.status_code} - {response.json()}")

    response = requests.get(f"{base_url}/users/john")
    print(f"GET /users/john: {response.status_code} - {response.json()}")

    # Test an undefined endpoint
    response = requests.get(f"{base_url}/undefined")
    print(f"GET /undefined: {response.status_code} - {response.json()}")

    # Test adding a new user with POST /add_user
    new_user = {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }
    response = requests.post(f"{base_url}/add_user", headers={"Content-Type": "application/json"}, data=json.dumps(new_user))
    print(f"POST /add_user: {response.status_code} - {response.json()}")

    # Verify the new user was added
    response = requests.get(f"{base_url}/users/alice")
    print(f"GET /users/alice: {response.status_code} - {response.json()}")

if __name__ == "__main__":
    test_flask_api()
