import json
import torch
from enum import Enum
from typing import Optional

from transformers import AutoTokenizer, AutoModelForCausalLM
from llama_cpp import Llama
from pydantic import BaseModel

from backend.memory import add_memory, get_memory
from backend.prompt import FIXING_PROMPT, SUGGESTION_PROMPT, WORKFLOW_PROMPT


# -------------------- Pydantic models --------------------
class PrivacyIssue(BaseModel):
    id: int
    issue: str
    location: str
    severity: str
    suggestion: str


class LLMResponse(BaseModel):
    issues: list[PrivacyIssue]
    raw_text: str
    fixed_code: Optional[str]


class Type(str, Enum):
    FIXING = "fixing"
    SUGGESTION = "suggestion"


class WorkFlow(BaseModel):
    type: Type


# -------------------- LLM setup --------------------

# llm = Llama(
#     model_path="./backend/ai/models/qwen2.5-coder-1.5b-instruct-q4_k_m.gguf",
#     n_ctx=2048,
#     n_threads=8,
# )

checkpoint = "deepseek-coder-1.3b-instruct"  # or your local path
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
llm = AutoModelForCausalLM.from_pretrained(
    checkpoint,
    torch_dtype=torch.float16,   # or bfloat16 if your hardware supports
    device_map="auto",           # "mps" for Apple Silicon, "cpu" otherwise
)

# -------------------- Helper --------------------
# def ask_llm(prompt: str, user_input: str, max_tokens: int = 512) -> str:
#     """Send prompt + memory + user input to LLM and return text output."""
#     context = f"{prompt}\n\nConversation so far:\n{get_memory(n_messages=5)}\n\nUser Input:\n{user_input}"
#     output = llm(context, max_tokens=max_tokens, stop=["</s>"])
#     text = output["choices"][0]["text"].strip()
#     add_memory("assistant", text)
#     return text

def ask_llm(prompt: str, user_input: str, max_tokens: int = 512) -> str:
    """Send prompt + memory + user input to LLM and return text output."""
    context = f"{prompt}\n\nConversation so far:\n{get_memory(n_messages=5)}\n\nUser Input:\n{user_input}"
    inputs = tokenizer(context, return_tensors="pt").to(llm.device)
    output_ids = llm.generate(
        **inputs,
        max_new_tokens=max_tokens,
        do_sample=False,  # greedy, disable sampling
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )
    full_output = tokenizer.decode(
        output_ids[0],
        skip_special_tokens=True,
        clean_up_tokenization_spaces=True,
    )
    text = full_output[len(context):].strip()
    add_memory("assistant", text)
    return text

# def ask_llm(prompt: str, user_input: str, max_tokens: int = 512) -> str:
#     """Send prompt + memory + user input to LLM and return text output."""
#     context = f"{prompt}\n\nConversation so far:\n{get_memory(n_messages=5)}"
#     messages = [
#         {
#             "role": "system",
#             "content": context,
#         },
#         {"role": "user", "content": user_input},
#     ]
#     prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
#     outputs = pipe(prompt, max_new_tokens=max_tokens, do_sample=False)
#     text = outputs[0]["generated_text"]
#     add_memory("assistant", text)
#     return text


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
        issues = [
            PrivacyIssue(
                id=1,
                issue="Parsing failed",
                location="",
                severity="low",
                suggestion=raw_text,
            )
        ]
    return LLMResponse(issues=issues, raw_text=raw_text, fixed_code=None)


def generate_code(user_input: str) -> str:
    return ask_llm(FIXING_PROMPT, user_input, max_tokens=2048)
