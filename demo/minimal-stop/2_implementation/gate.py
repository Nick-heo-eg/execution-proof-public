from decision import DecisionToken

def judgment_gate(user_input: str) -> DecisionToken:
    """
    Deterministic execution boundary.

    Returns:
        DecisionToken("STOP") if input contains forbidden keywords
        DecisionToken("ALLOW") otherwise
    """
    forbidden_keywords = ["send", "delete", "execute"]

    for word in forbidden_keywords:
        if word in user_input.lower():
            return DecisionToken("STOP")

    return DecisionToken("ALLOW")
