# utils/api_utils.py
import requests

BASE_URL = "http://localhost:4005/api"

def get_all(endpoint: str):
    return requests.get(f"{BASE_URL}/{endpoint}").json()

def get_all_with_token(endpoint: str, headers):
    return requests.get(f"{BASE_URL}/{endpoint}", headers=headers).json()

def get_by_id(endpoint: str, item_id: int):
    return requests.get(f"{BASE_URL}/{endpoint}/{item_id}").json()

def create(endpoint: str, data: dict):
    return requests.post(f"{BASE_URL}/{endpoint}", json=data).json()

def update(endpoint: str, item_id: int, data: dict):
    return requests.put(f"{BASE_URL}/{endpoint}/{item_id}", json=data).json()

def delete(endpoint: str, item_id: int):
    return requests.delete(f"{BASE_URL}/{endpoint}/{item_id}").json()
