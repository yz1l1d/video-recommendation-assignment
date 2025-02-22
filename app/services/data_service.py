import os
import requests
from dotenv import load_dotenv

load_dotenv()

FLIC_TOKEN = os.getenv("FLIC_TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL")
HEADERS = {"Flic-Token": FLIC_TOKEN}

def fetch_user_data(endpoint: str, params: dict = None):
    url = f"{API_BASE_URL}{endpoint}"
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()

def get_user_feed(username: str):
    # Example: Fetch viewed posts as a proxy for preferences
    params = {"page": 1, "page_size": 1000}
    viewed_posts = fetch_user_data("/posts/view", params)
    # Placeholder: Replace with DNN inference
    return ["video1", "video2", "video3"]  # Mock recommendations

def get_category_feed(username: str, category_id: str):
    # Placeholder: Filter by category_id
    params = {"page": 1, "page_size": 1000}
    all_posts = fetch_user_data("/posts/summary/get", params)
    return [post for post in all_posts if post.get("category_id") == category_id][:3]