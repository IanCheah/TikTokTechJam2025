from llama_cpp import Llama
from prompt import WORKFLOW_PROMPT, SUGGESTION_PROMPT, FIXING_PROMPT
from memory import get_memory, add_memory
import json
from pydantic import BaseModel
from typing import List

# -------------------- Pydantic models --------------------
class PrivacyIssue(BaseModel):
    id: int
    issue: str
    location: str
    severity: str
    suggestion: str

class LLMResponse(BaseModel):
    issues: List[PrivacyIssue]
    raw_text: str

# -------------------- LLM setup --------------------

llm = Llama(model_path="./models/codellama-7b-instruct.Q4_K_M.gguf",
             n_ctx=2048,  
             n_threads=8)


# -------------------- Helper --------------------
def ask_llm(prompt: str, user_input: str, max_tokens: int = 512) -> str:
    """Send prompt + memory + user input to LLM and return text output."""
    context = f"{prompt}\n\nConversation so far:\n{get_memory(n_messages=5)}\n\nUser Input:\n{user_input}"
    output = llm(context, max_tokens=max_tokens, stop=["</s>"])
    text = output["choices"][0]["text"].strip()
    add_memory("assistant", text)
    return text

# -------------------- Workflow --------------------
def workflow_decider(user_input: str) -> str:
    add_memory("user", user_input)
    return ask_llm(WORKFLOW_PROMPT, user_input)

def generate_suggestion(user_input: str) -> LLMResponse:
    raw_text = ask_llm(SUGGESTION_PROMPT, user_input)
    try:
        # attempt to parse JSON from LLM
        issues = json.loads(raw_text)
        issues = [PrivacyIssue(**i) for i in issues]
    except Exception:
        # fallback: raw text as single entry if JSON parsing fails
        issues = [PrivacyIssue(id=1, issue="Parsing failed", location="", severity="low", suggestion=raw_text)]
    return LLMResponse(issues=issues, raw_text=raw_text)

def generate_code(user_input: str) -> str:
    return ask_llm(FIXING_PROMPT, user_input, max_tokens=2048)
