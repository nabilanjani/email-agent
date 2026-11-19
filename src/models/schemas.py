
VALID_ACTIONS = {
    "search_emails",
    "list_emails",
    "read_email"
}

VALID_CATEGORIES = {
    "invoice",
    "schedule",
    "meeting",
    "promotion",
    "payment",
    "general"
}

VALID_STATUSES = {
    "unpaid",
    "paid",
    None
}

VALID_DATE_PERIODS = {
    "this_month",
    "last_month",
    "this_week",
    "next_week",
    "today",
    "all_time",
    "unspecified"
}


def validate_intent(intent):

    required_fields = {
        "action",
        "category",
        "status",
        "date_period",
        "search_query",
        "needs_clarification"
    }

    if not isinstance(intent, dict):
        raise ValueError("Intent harus berupa dictionary")

    if not required_fields.issubset(intent.keys()):
        raise ValueError("Field intent tidak lengkap")

    if intent["action"] not in VALID_ACTIONS:
        raise ValueError("Action tidak valid")

    if intent["category"] not in VALID_CATEGORIES:
        raise ValueError("Category tidak valid")

    if intent["status"] not in VALID_STATUSES:
        raise ValueError("Status tidak valid")

    if intent["date_period"] not in VALID_DATE_PERIODS:
        raise ValueError("Date period tidak valid")

    if not isinstance(intent["needs_clarification"], bool):
        raise ValueError("needs_clarification harus boolean")

    if not isinstance(intent["search_query"], str):
        raise ValueError("search_query harus berupa string")

    return intent
