from fastapi import APIRouter

from backend.chat import chat
from backend.llm import LLMResponse

router = APIRouter()


@router.post("/chat", response_model=LLMResponse)
def content_content(request: str) -> LLMResponse:
    return chat(request)
