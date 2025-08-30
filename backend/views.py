from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

from backend.chat import chat
from backend.llm import LLMResponse

router = APIRouter()


class ChatRequest(BaseModel):
    type: str
    request: str


@router.post("/chat", response_model=LLMResponse)
def content_content(request: ChatRequest) -> Optional[LLMResponse]:
    return chat(request.type, request.request)
