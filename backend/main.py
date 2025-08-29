from fastapi import FastAPI

from backend.views import router as api_router

app = FastAPI(title="Data Sanitisation API")
app.include_router(api_router, prefix="/chat")


@app.get("/")
async def root():
    return {
        "message": "Data Sanitization API is running",
    }
