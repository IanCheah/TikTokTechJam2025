from backend.llm import (
    LLMResponse,
    generate_code,
    generate_suggestion,
    workflow_decider,
)


def chat(user_input: str) -> LLMResponse:
    print("=== Privacy Checker Chatbot ===")

    # user_input = input("\nEnter your code: ")

    task = workflow_decider(user_input)
    print(task)
    print("HELLO WORLD")

    if "suggestion" in task.lower():
        response = generate_suggestion(user_input)
        print("\n--- Privacy Issues Found ---")
        for issue in response.issues:
            print(
                f"{issue.id}. {issue.issue} (Location: {issue.location}) - Severity: {issue.severity} - Suggestion: {issue.suggestion}"
            )
    elif "fixing" in task.lower():
        response = generate_code(user_input)
        print("\n--- Fixed Code ---")
        print(response)
    else:
        print("\n Could not determine the task.")
    return response

