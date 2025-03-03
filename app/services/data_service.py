import os
import requests
from dotenv import load_dotenv

load_dotenv()

FLIC_TOKEN = os.getenv("FLIC_TOKEN") or ""
API_BASE_URL = os.getenv("API_BASE_URL") or ""
HEADERS = {"Flic-Token": FLIC_TOKEN}

def fetch_user_data(endpoint: str, params: dict = None):
    url = f"{API_BASE_URL}{endpoint}"
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()

def get_user_feed(username: str):
    params = {"page": 1, "page_size": 1000}
    viewed_posts = fetch_user_data("/posts/view", params)
    return ["video1", "video2", "video3"]  # Mock recommendations

def get_category_feed(username: str, category_id: str):
    params = {"page": 1, "page_size": 1000}
    all_posts = fetch_user_data("/posts/summary/get", params).get("posts", [])
    filtered_posts = [post for post in all_posts if str(post.get("category_id", "")) == category_id]
    return [post.get("post_id", "unknown") for post in filtered_posts[:3]]