def judgment_gate(user_input: str) -> str:
    """
    Deterministic execution boundary.

    Returns:
        "STOP" if input contains forbidden keywords
        "ALLOW" otherwise
    """
    forbidden_keywords = ["send", "delete", "execute"]

    for word in forbidden_keywords:
        if word in user_input.lower():
            return "STOP"

    return "ALLOW"
