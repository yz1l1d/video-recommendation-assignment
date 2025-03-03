from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.api.routes import router  # Import API routes

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Video Recommendation Engine",
    description="A personalized video recommendation system",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs"
)

# Include API routes
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Video Recommendation Engine!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)