import json
import re

from backend.utils import LLMResponse, PrivacyIssue


def parse_llm_response(raw_text: str) -> LLMResponse:
    """
    Parses raw LLM output (possibly with extra words) into an LLMResponse object.
    Only keeps the fields expected by PrivacyIssue.
    """
    # Extract first JSON array/object using regex
    match = re.search(r"(\[.*\]|\{.*\})", raw_text, re.DOTALL)
    if match:
        json_str = match.group(0)
        try:
            data = json.loads(json_str)

            # Ensure data is a list
            if isinstance(data, dict):
                data = [data]

            issues = []
            for item in data:
                # Only keep expected fields; convert id to int
                try:
                    issues.append(
                        PrivacyIssue(
                            id=int(item.get("id", 0)),
                            issue=item.get("issue", ""),
                            location=item.get("location", ""),
                            severity=item.get("severity", ""),
                            suggestion=item.get("suggestion", ""),
                        )
                    )
                except Exception:
                    # Fallback single issue if a PrivacyIssue cannot be created
                    issues.append(
                        PrivacyIssue(
                            id=0,
                            issue="Failed to parse individual issue",
                            location="",
                            severity="low",
                            suggestion=str(item),
                        )
                    )

            return LLMResponse(issues=issues, raw_text=raw_text, fixed_code=None)

        except json.JSONDecodeError:
            # Failed to parse JSON
            return LLMResponse(
                issues=[
                    PrivacyIssue(
                        id=0,
                        issue="Failed to parse JSON",
                        location="",
                        severity="low",
                        suggestion=raw_text,
                    )
                ],
                raw_text=raw_text,
                fixed_code=None,
            )
    else:
        # No JSON found in text
        return LLMResponse(
            issues=[
                PrivacyIssue(
                    id=0,
                    issue="No JSON found",
                    location="",
                    severity="low",
                    suggestion=raw_text,
                )
            ],
            raw_text=raw_text,
            fixed_code=None,
        )
