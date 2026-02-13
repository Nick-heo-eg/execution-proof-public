from gate import judgment_gate
from executor import execute_action
import datetime
import os

LOG_FILE = "execution.log"

def log(message):
    """Write message to log file with timestamp."""
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")

def clear_log():
    """Remove previous log file if exists."""
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

def main():
    clear_log()

    # Scenario: User attempts to send message
    user_input = "Send message to admin"

    # Judgment gate evaluates BEFORE execution
    decision = judgment_gate(user_input)

    log(f"INPUT: {user_input}")
    log(f"DECISION: {decision.status}")

    # Execution requires authority token
    try:
        execute_action(user_input, decision)
        log("EXECUTION: PERFORMED")
    except PermissionError as e:
        log(f"EXECUTION: BLOCKED ({str(e)})")

    print("Run complete. Check execution.log")

if __name__ == "__main__":
    main()
