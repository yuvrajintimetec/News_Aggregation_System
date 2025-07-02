import requests
import os
from dotenv import load_dotenv

load_dotenv()


BASE_URL = os.getenv("BASE_URL")

def get_all(endpoint: str):
    return requests.get(f"{BASE_URL}/{endpoint}").json()

def get_all_with_token(endpoint: str, headers):
    return requests.get(f"{BASE_URL}/{endpoint}", headers=headers).json()

def get_by_id(endpoint: str, item_id: int):
    return requests.get(f"{BASE_URL}/{endpoint}/{item_id}").json()

def get_by_id_with_token(endpoint: str, item_id: int, headers):
    return requests.get(f"{BASE_URL}/{endpoint}/{item_id}",headers=headers).json()

def create(endpoint: str, data: dict):
    return requests.post(f"{BASE_URL}/{endpoint}", json=data).json()

def create_with_token(endpoint: str, data: dict, headers):
    return requests.post(f"{BASE_URL}/{endpoint}", json=data, headers=headers).json()

def update(endpoint: str, item_id: int, data: dict):
    return requests.put(f"{BASE_URL}/{endpoint}/{item_id}", json=data).json()

def update_with_token(endpoint: str, item_id: int, data: dict, headers):
    return requests.put(f"{BASE_URL}/{endpoint}/{item_id}", json=data,headers=headers).json()

def delete(endpoint: str, item_id: int):
    return requests.delete(f"{BASE_URL}/{endpoint}/{item_id}").json()

def delete_with_token(endpoint: str, item_id: int, headers):
    return requests.delete(f"{BASE_URL}/{endpoint}/{item_id}",headers=headers).json()
