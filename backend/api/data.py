from api.models import Suggestion, SuggestionType

# TODO: Remove the data when chatbot is ready

DUMMY_SUGGESTIONS_TEXT = [
    Suggestion(
        id="sugg_1",
        type=SuggestionType.EMAIL,
        text_snippet="john.doe@example.com",
    ),
    Suggestion(
        id="sugg_2",
        type=SuggestionType.PHONE,
        text_snippet="555-123-4567",
    ),
    Suggestion(
        id="sugg_3",
        type=SuggestionType.API_KEY,
        text_snippet="sk_1234567890abcdef",
    ),
]


DUMMY_SUGGESTIONS_IMAGE = [
    Suggestion(
        id="sugg_1",
        type=SuggestionType.FACE,
        text_snippet="Face detected at coordinates (120, 45, 180, 120)",
    ),
    Suggestion(
        id="sugg_2",
        type=SuggestionType.LICENSE_PLATE,
        text_snippet="License plate detected at coordinates (240, 80, 300, 110)",
    ),
]

DUMMY_SANITIZED_TEXT = "My email is ********* and my phone is (555) 123-4567. My API key is sk_fake_123456."
DUMMY_SANITIZED_IMAGE = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
