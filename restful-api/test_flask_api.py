import requests

def test_flask_api():
    base_url = "http://localhost:5000"
    
    # Test home endpoint
    response = requests.get(base_url)
    print(f"GET /: {response.status_code} - {response.text}")
    assert response.status_code == 200
    assert response.text == "Welcome to the Flask API!"
    
    # Test data endpoint when no users are added
    response = requests.get(f"{base_url}/data")
    print(f"GET /data: {response.status_code} - {response.json()}")
    assert response.status_code == 200
    assert response.json() == []

    # Test adding a user to the API
    new_user = {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }
    response = requests.post(f"{base_url}/add_user", json=new_user)
    print(f"POST /add_user: {response.status_code} - {response.json()}")
    assert response.status_code == 201
    assert response.json()["message"] == "User added"
    assert response.json()["user"] == new_user

    # Test the data route of the API after adding a user
    response = requests.get(f"{base_url}/data")
    print(f"GET /data: {response.status_code} - {response.json()}")
    assert response.status_code == 200
    assert response.json() == ["alice"]

    # Test getting a user from the API
    response = requests.get(f"{base_url}/users/alice")
    print(f"GET /users/alice: {response.status_code} - {response.json()}")
    assert response.status_code == 200
    assert response.json() == new_user
    
    # Test getting a user that does not exist
    response = requests.get(f"{base_url}/users/unknown")
    print(f"GET /users/unknown: {response.status_code} - {response.json()}")
    assert response.status_code == 404
    assert response.json()["error"] == "User not found"
    
    # Test the status route of the API
    response = requests.get(f"{base_url}/status")
    print(f"GET /status: {response.status_code} - {response.text}")
    assert response.status_code == 200
    assert response.text == "OK"

    # Test adding a user without a username
    incomplete_user = {
        "name": "Bob",
        "age": 27,
        "city": "Miami"
    }
    response = requests.post(f"{base_url}/add_user", json=incomplete_user)
    print(f"POST /add_user (no username): {response.status_code} - {response.json()}")
    assert response.status_code == 400
    assert response.json()["error"] == "Username is required"

    # Test adding a user with a duplicate username
    duplicate_user = {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }
    response = requests.post(f"{base_url}/add_user", json=duplicate_user)
    print(f"POST /add_user (duplicate username): {response.status_code} - {response.json()}")
    assert response.status_code == 400
    assert response.json()["error"] == "User already exists"

if __name__ == "__main__":
    test_flask_api()
