import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")
FLIC_TOKEN = os.getenv("FLIC_TOKEN")

HEADERS = {"Flic-Token": FLIC_TOKEN}

def fetch_external_data(endpoint: str):
    """Fetch data from an external API endpoint."""
    url = f"{API_BASE_URL}{endpoint}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def get_all_posts():
    """Fetch and process post data"""
    data = fetch_external_data("/posts/summary/get?page=1&page_size=1000")
    if data:
        return [{"id": post["id"], 
                 "title": post["title"], 
                 "content": post["content"], 
                 "category": post.get("category", "unknown")
                 } for post in data.get("posts", [])]
    return []

def get_all_users():
    """Fetch and process user data"""
    data = fetch_external_data("/users/get_all?page=1&page_size=1000")
    if data:
        return [{"id": user["id"], 
                 "username": user["username"], 
                 "email": user.get("email", ""), 
                 "full_name": user.get("full_name", "")
                 } for user in data.get("users", [])]
    return []
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")
FLIC_TOKEN = os.getenv("FLIC_TOKEN")

HEADERS = {"Flic-Token": FLIC_TOKEN}

def fetch_external_data(endpoint: str):
    """Fetch data from an external API endpoint."""
    url = f"{API_BASE_URL}{endpoint}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise error for HTTP failures
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def get_all_posts():
    """Fetch and process post data"""
    data = fetch_external_data("/posts/summary/get?page=1&page_size=1000")
    if data:
        return [{"id": post["id"], 
                 "title": post["title"], 
                 "content": post.get("content",""), 
                 "category": str(post.get("category", "General"))
                 }for post in data.get("posts", [])]             
    return []

def get_all_users():
    """Fetch and process user data"""
    data = fetch_external_data("/users/get_all?page=1&page_size=1000")
    if data:
        return [{"id": user["id"], 
                 "username": user["username"], 
                 "email": user.get("email", ""), 
                 "full_name": user.get("full_name", "")
                 } for user in data.get("users", [])]
    return []