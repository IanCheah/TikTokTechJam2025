from typing import Optional

from backend.llm import (
    LLMResponse,
    generate_code,
    generate_suggestion,
    workflow_decider,
)
from backend.memory import add_memory
from backend.service import parse_llm_response


def chat(type: str, user_input: str) -> Optional[LLMResponse]:
    print("=== Privacy Checker Chatbot ===")

    # user_input = input("\nEnter your code: ")

    # task = workflow_decider(user_input)
    # task = "suggestion"
    # print(task)
    print(type)
    print("HELLO WORLD")
    if "suggestion" == type:
        response = generate_suggestion(user_input)
        print("\n--- Privacy Issues Found ---")
        for issue in response.issues:
            print(
                f"{issue.id}. {issue.issue} (Location: {issue.location}) - Severity: {issue.severity} - Suggestion: {issue.suggestion} - Implications: {issue.implications}"
            )
        return response
    elif "fixing" == type:
        response = generate_code(user_input)
        print("\n--- Fixed Code ---")
        print(response)
        return parse_llm_response(response)
    else:
        print("\n Could not determine the task.")
