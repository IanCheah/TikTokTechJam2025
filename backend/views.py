from fastapi import APIRouter
from pydantic import BaseModel

from backend.chat import chat
from backend.llm import LLMResponse

router = APIRouter()


class ChatRequest(BaseModel):
    request: str


@router.post("/chat", response_model=LLMResponse)
def content_content(request: ChatRequest) -> LLMResponse:
    return chat(request.request)
