from uuid import uuid4

from api.data import (
    DUMMY_SANITIZED_IMAGE,
    DUMMY_SANITIZED_TEXT,
    DUMMY_SUGGESTIONS_IMAGE,
    DUMMY_SUGGESTIONS_TEXT,
)
from api.models import (
    AnalyseRequest,
    AnalyseResponse,
    ChatRequest,
    ChatResponse,
    ContentType,
    SanitiseRequest,
    SanitiseResponse,
)
from fastapi import APIRouter, HTTPException

current_session = None

router = APIRouter()


@router.post("/api/analyse", response_model=AnalyseResponse)
def analyse_content(request: AnalyseRequest):
    global current_session

    session_id = str(uuid4())

    # TODO: make calls to chatbot
    # By right: send the original data to the chatbot, and generate response
    if request.content_type == ContentType.TEXT:
        suggestions = DUMMY_SUGGESTIONS_TEXT
    else:
        suggestions = DUMMY_SUGGESTIONS_IMAGE

    current_session = {
        "session_id": session_id,
        "content_type": request.content_type,
        "original_data": request.original_data,
        "suggestions": suggestions,
    }

    # send request to chatbot, obtain the response
    return AnalyseResponse(session_id=session_id, suggestions=suggestions)


@router.post("/api/sanitise", response_model=SanitiseResponse)
def sanitise_content(request: SanitiseRequest):
    global current_session

    if not current_session or current_session["session_id"] != request.session_id:
        raise HTTPException(status_code=404)

    # TODO: make call to chatbot
    if current_session["content_type"] == ContentType.TEXT:
        sanitised_data = DUMMY_SANITIZED_TEXT
    else:
        sanitised_data = DUMMY_SANITIZED_IMAGE

    return SanitiseResponse(sanitised_data=sanitised_data, status="success")


@router.post("/api/chat", response_model=ChatResponse)
def chat_with_bot(request: ChatRequest):
    global current_session

    if not current_session or current_session["session_id"] != request.session_id:
        raise HTTPException(status_code=404)

    # TODO: replace this to call the chatbot
    message = request.message.lower()

    # Simple hardcoded responses based on message content
    message = request.message.lower()

    if "phone" in message:
        response_msg = "I found a phone number in your content: 555-123-4567"
    elif "email" in message:
        response_msg = "I found an email address in your content: john.doe@example.com"
    elif "remove" in message and "all" in message:
        response_msg = "I've removed all sensitive data from your content."
    else:
        response_msg = (
            "I've processed your request and updated the suggestions accordingly."
        )

    return ChatResponse(message=response_msg, new_suggestions=None)
