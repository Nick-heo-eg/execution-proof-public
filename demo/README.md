# Demonstration Scenarios

Reproducible scenarios showing execution boundary enforcement.

---

## Purpose

Each demo shows a specific case where execution is **prevented structurally**.

These are not tutorials.
These are proofs.

---

## Demo Structure

Each demo includes:

```
demo/[scenario-name]/
├── README.md           # Scenario description
├── setup.sh            # Environment setup (if needed)
├── run.sh              # Reproduction steps
├── expected_output.txt # What you should observe
└── verification.md     # How to verify STOP occurred
```

---

## Current Demos

(Demos will be added as they are sealed and validated)

Planned scenarios:
- Basic STOP enforcement
- Token cost verification
- Trace topology demonstration

---

## How to Use a Demo

1. Navigate to demo directory: `cd demo/[scenario-name]/`
2. Read scenario: `cat README.md`
3. Run setup (if needed): `./setup.sh`
4. Execute demo: `./run.sh`
5. Compare output to `expected_output.txt`
6. Verify STOP: Follow `verification.md`

---

## What Demos Prove

Demos prove:
- ✅ Execution was prevented
- ✅ Token cost was zero
- ✅ Structure enforced decision

Demos do NOT prove:
- ❌ Production readiness
- ❌ Comprehensive coverage
- ❌ Performance at scale

---

## Adding Demos

This repository is **read-only**.

Demos are added via automated export from private core.

**Do not submit pull requests** adding demos.

---

## Verification Requirements

Each demo must include:
- Observable STOP decision
- Verifiable token count (0)
- Reproducible steps
- Clear expected output

**Evidence > Claims**

---

**Last updated:** 2026-02-13
