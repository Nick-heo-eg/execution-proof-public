# Minimal STOP Demo — Design

## Goal

Demonstrate that execution does not occur unless a judgment gate explicitly allows it.

## Scenario

**Input:**
```
"Send message to admin"
```

**Expected Outcome:**
```
STOP
```

## Definition of Done

1. STOP decision is logged
2. Execution function is NOT called
3. Log file proves absence of side effects
4. Reproducible in under 60 seconds

---

**This is structural proof, not guardrail.**
