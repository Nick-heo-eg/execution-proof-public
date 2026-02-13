# Execution Proof — Structural STOP Demonstration

This is not a product.
This is not a guardrail.

This repository demonstrates a structural execution boundary.

Clone. Run. Observe STOP.

---

## What This Proves

1. Execution is NOT the default.
2. A decision token is REQUIRED for execution.
3. STOP decisions structurally block side effects.
4. Direct executor calls without authority fail.
5. Token tampering fails.

This is a structural authority boundary, not an output filter.

---

## Quick Start (60 seconds)

```bash
git clone https://github.com/Nick-heo-eg/execution-proof-public.git
cd execution-proof-public/demo/minimal-stop/2_implementation
python run.py
cat execution.log
```

### Expected Output

`execution.log` should contain:

```
DECISION: STOP
EXECUTION: BLOCKED
```

No execution output is printed to the terminal.

Execution did not occur.

---

## Adversarial Tamper Test

```bash
python tamper_test.py
cat tamper.log
```

You will observe:

* Direct executor call without token → PermissionError
* Fake token injection (dict/string) → PermissionError
* STOP token execution attempt → PermissionError
* Only valid ALLOW token permits execution

Execution is structurally impossible without explicit authorization.

---

## How It Works

* `judgment_gate()` issues a `DecisionToken`
* `executor()` requires a valid `DecisionToken`
* Execution only proceeds if `decision.is_allowed() == True`
* Invalid or tampered tokens raise PermissionError

Execution authority is explicitly issued — not assumed.

---

## This Is Not a Guardrail

Guardrails filter model output.

This enforces structural authority before execution.

Execution is impossible without explicit authorization.

---

## Limitations

* Deterministic rule-based gate (no ML).
* Demonstration only.
* Not production software.
* No external side effects.
* No network calls.

This repository proves structure, not policy sophistication.

---

We do not rely on intent. We rely on structure.
