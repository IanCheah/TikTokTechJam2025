import json
from enum import Enum
from typing import Optional

from llama_cpp import Llama
from pydantic import BaseModel

from backend.memory import add_memory, get_memory
from backend.prompt import FIXING_PROMPT, SUGGESTION_PROMPT, WORKFLOW_PROMPT
from backend.service import parse_llm_response
from backend.utils import LLMResponse


# -------------------- LLM setup --------------------

llm = Llama(
    model_path="qwen2.5-coder-1.5b-instruct-q4_k_m.gguf",
    n_ctx=2048,
    n_threads=8,
)


# -------------------- Helper --------------------
def ask_llm(prompt: str, user_input: str, max_tokens: int = 512) -> str:
    """Send prompt + memory + user input to LLM and return text output."""
    context = (
        f"{prompt}\n\nConversation so far:\n{get_memory()}\n\nUser Input:\n{user_input}"
    )
    output = llm(context, max_tokens=max_tokens, stop=["</s>"])
    text = output["choices"][0]["text"].strip()
    add_memory("user", user_input)
    add_memory("assistant", text)
    return text


# -------------------- Workflow --------------------
def workflow_decider(user_input: str) -> str:
    return ask_llm(WORKFLOW_PROMPT, user_input)


def generate_suggestion(user_input: str) -> LLMResponse:
    raw_text = ask_llm(SUGGESTION_PROMPT, user_input)
    return parse_llm_response(raw_text)


def generate_code(user_input: str) -> str:
    return ask_llm(FIXING_PROMPT, user_input, max_tokens=2048)
