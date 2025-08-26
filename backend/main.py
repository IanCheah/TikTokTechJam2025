from api.views import router as api_router
from fastapi import FastAPI

app = FastAPI(title="Data Sanitisation API")
app.include_router(api_router, prefix="/api")


@app.get("/")
async def root():
    return {
        "message": "Data Sanitization API is running",
    }
