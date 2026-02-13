from decision import DecisionToken

def execute_action(user_input: str, decision: DecisionToken):
    """
    Simulated side effect.

    Execution requires a valid DecisionToken.
    Raises PermissionError if token is invalid or STOP.
    """
    if not isinstance(decision, DecisionToken):
        raise PermissionError("Invalid decision token.")

    if not decision.is_allowed():
        raise PermissionError("Execution denied: STOP decision.")

    print(f"[EXECUTION] Action executed: {user_input}")
