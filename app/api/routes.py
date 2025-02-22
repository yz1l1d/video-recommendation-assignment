from fastapi import APIRouter, HTTPException
from app.services.data_service import get_user_feed, get_category_feed

router = APIRouter()

@router.get("/feed")
async def get_personalized_feed(username: str):
    try:
        feed = get_user_feed(username)
        return {"username": username, "recommendations": feed}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/feed/category")
async def get_category_based_feed(username: str, category_id: str):
    try:
        feed = get_category_feed(username, category_id)
        return {"username": username, "category_id": category_id, "recommendations": feed}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))