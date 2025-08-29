from typing import List
from pydantic import BaseModel
from datetime import datetime

class Message(BaseModel):
    role: str  # "user" or "assistant"
    content: str
    timestamp: datetime

conversation_memory: List[Message] = []

def add_memory(role: str, content: str):
    conversation_memory.append(Message(role=role, content=content, timestamp=datetime.now()))

def get_memory(n_messages: int = None):
    """Return last n_messages as concatenated string for context."""
    msgs = conversation_memory if n_messages is None else conversation_memory[-n_messages:]
    return "\n".join([f"{m.role}: {m.content}" for m in msgs])
