class DecisionToken:
    """
    Authority token for execution.

    Execution cannot occur without a valid token.
    """
    def __init__(self, status: str):
        self.status = status

    def is_allowed(self) -> bool:
        return self.status == "ALLOW"
