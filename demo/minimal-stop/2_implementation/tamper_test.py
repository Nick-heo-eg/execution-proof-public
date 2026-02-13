from executor import execute_action
from decision import DecisionToken
import datetime
import os

LOG_FILE = "tamper.log"

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")

def clear_log():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

def case(name, fn):
    log(f"CASE START: {name}")
    try:
        fn()
        log(f"CASE RESULT: PASS (unexpected)")
    except Exception as e:
        log(f"CASE RESULT: BLOCKED ({type(e).__name__}: {str(e)})")
    log(f"CASE END: {name}")
    log("---")

def main():
    clear_log()

    # 1) no token
    case("no-token-direct-call", lambda: execute_action("delete server files", None))

    # 2) fake token (dict)
    fake = {"status": "ALLOW"}
    case("fake-token-dict", lambda: execute_action("delete server files", fake))

    # 3) STOP token
    stop_token = DecisionToken("STOP")
    case("stop-token", lambda: execute_action("delete server files", stop_token))

    # 4) ALLOW token (should succeed)
    allow_token = DecisionToken("ALLOW")
    case("allow-token", lambda: execute_action("print hello", allow_token))

    print("Tamper test complete. Check tamper.log")

if __name__ == "__main__":
    main()
