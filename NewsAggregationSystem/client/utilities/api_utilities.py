import requests
import os
from dotenv import load_dotenv

load_dotenv()


BASE_URL = os.getenv("BASE_URL")

def get_all(endpoint: str):
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        return {"error": "Server is not reachable."}
    except requests.exceptions.HTTPError as err:
        return {"error": f"HTTP error occurred: {err}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}


def get_all_with_token(endpoint: str, headers):
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        return {"error": "Server is not reachable."}
    except requests.exceptions.HTTPError as err:
        return {"error": f"HTTP error occurred: {err}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}


def get_by_id(endpoint: str, item_id: int):
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}/{item_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        return {"error": "Server is not reachable."}
    except requests.exceptions.HTTPError as err:
        return {"error": f"HTTP error occurred: {err}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}


def get_by_id_with_token(endpoint: str, item_id: int, headers):
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}/{item_id}", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        return {"error": "Server is not reachable."}
    except requests.exceptions.HTTPError as err:
        return {"error": f"HTTP error occurred: {err}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}


def create(endpoint: str, data: dict):
    try:
        response = requests.post(f"{BASE_URL}/{endpoint}", json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        return {"error": "Server is not reachable."}
    except requests.exceptions.HTTPError as err:
        return {"error": f"HTTP error occurred: {err}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}


def create_with_token(endpoint: str, data: dict, headers):
    try:
        response = requests.post(f"{BASE_URL}/{endpoint}", json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        return {"error": "Server is not reachable."}
    except requests.exceptions.HTTPError as err:
        return {"error": f"HTTP error occurred: {err}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}


def update(endpoint: str, item_id: int, data: dict):
    try:
        response = requests.put(f"{BASE_URL}/{endpoint}/{item_id}", json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        return {"error": "Server is not reachable."}
    except requests.exceptions.HTTPError as err:
        return {"error": f"HTTP error occurred: {err}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}


def update_with_token(endpoint: str, item_id: int, data: dict, headers):
    try:
        response = requests.put(f"{BASE_URL}/{endpoint}/{item_id}", json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        return {"error": "Server is not reachable."}
    except requests.exceptions.HTTPError as err:
        return {"error": f"HTTP error occurred: {err}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}


def delete(endpoint: str, item_id: int):
    try:
        response = requests.delete(f"{BASE_URL}/{endpoint}/{item_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        return {"error": "Server is not reachable."}
    except requests.exceptions.HTTPError as err:
        return {"error": f"HTTP error occurred: {err}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}


def delete_with_token(endpoint: str, item_id: int, headers):
    try:
        response = requests.delete(f"{BASE_URL}/{endpoint}/{item_id}", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        return {"error": "Server is not reachable."}
    except requests.exceptions.HTTPError as err:
        return {"error": f"HTTP error occurred: {err}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}
