"""
1. function on highlighting difference in code
2. mask sensitive informationj
3. scorer function
"""

from enum import Enum
from typing import Optional

from pydantic import BaseModel


# -------------------- Pydantic models --------------------
class PrivacyIssue(BaseModel):
    id: int
    issue: str
    location: str
    severity: str
    suggestion: str
    implications: str


class LLMResponse(BaseModel):
    issues: list[PrivacyIssue]
    raw_text: str
    fixed_code: Optional[str]


class Type(str, Enum):
    FIXING = "fixing"
    SUGGESTION = "suggestion"


class WorkFlow(BaseModel):
    type: Type
