# Minimal STOP Demo

This is not a product.
This is not a guardrail.
This is a structural execution boundary.

---

## Run

```bash
cd 2_implementation
python run.py
```

---

## Expected Result

1. Terminal does NOT print execution message
2. `execution.log` contains:

```
DECISION: STOP
EXECUTION: BLOCKED
```

No side effects occurred.

---

## What This Proves

- Execution decision occurs **before** execution
- STOP prevents execution, not rollback
- Execution is **conditional**, not default

---

## Verification

Open `execution.log` and verify:
- INPUT line exists
- DECISION line shows STOP
- EXECUTION line shows BLOCKED
- No "[EXECUTION]" output in terminal

---

## Tamper Test (adversarial)

```bash
cd 2_implementation
python tamper_test.py
cat tamper.log
```

**Expected:**
- `no-token-direct-call` → BLOCKED (PermissionError)
- `fake-token-dict` → BLOCKED (PermissionError)
- `stop-token` → BLOCKED (Execution denied)
- `allow-token` → EXECUTION printed (authority granted)

This proves execution cannot bypass authority issuance.

---

**This is observable evidence, not claims.**
