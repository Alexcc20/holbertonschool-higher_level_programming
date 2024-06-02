import requests

def test_api():
    base_url = "http://localhost:8000"

    # Test the root endpoint
    response = requests.get(base_url)
    print(f"GET /: {response.status_code} - {response.text}")

    # Test the /data endpoint
    response = requests.get(f"{base_url}/data")
    print(f"GET /data: {response.status_code} - {response.json()}")

    # Test the /status endpoint
    response = requests.get(f"{base_url}/status")
    print(f"GET /status: {response.status_code} - {response.json()}")

    # Test an undefined endpoint
    response = requests.get(f"{base_url}/undefined")
    print(f"GET /undefined: {response.status_code} - {response.json()}")

if __name__ == "__main__":
    test_api()
