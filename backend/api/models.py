from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ActionType(str, Enum):
    MASK = "mask"
    REMOVE = "remove"
    FAKE = "fake"


class ContentType(str, Enum):
    TEXT = "text"
    IMAGE = "image"


class SuggestionType(str, Enum):
    EMAIL = "email"
    PHONE = "phone"
    API_KEY = "api_key"
    LICENSE_PLATE = "license_plate"
    FACE = "face"
    CREDIT_CARD = "credit_card"


"""
When user uploads the image/code
"""


class AnalyseRequest(BaseModel):
    content_type: ContentType
    original_data: str


class Suggestion(BaseModel):
    id: str
    type: SuggestionType
    text_snippet: str


class AnalyseResponse(BaseModel):
    session_id: str
    suggestions: list[Suggestion]


"""
When user selects the action to be performed
"""


class ActionRequest(BaseModel):
    suggestion_id: str
    action: ActionType


class SanitiseRequest(BaseModel):
    session_id: str
    actions: list[ActionRequest]


class SanitiseResponse(BaseModel):
    sanitised_data: str
    status: str


"""
When user chats
"""


class ChatRequest(BaseModel):
    session_id: str
    message: str


class ChatResponse(BaseModel):
    message: str
    new_suggestions: Optional[list[Suggestion]] = None
