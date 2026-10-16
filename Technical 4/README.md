# Smartphone Diagnostic System: Rule-Based & Case-Based Reasoning

A Python implementation demonstrating two core Artificial Intelligence reasoning paradigms: **Rule-Based Reasoning (RBR)** and **Case-Based Reasoning (CBR)** to diagnose, manage, and troubleshoot smartphone hardware and software issues.

---

## Features

### Part 1 & 2: Rule-Based Reasoning (RBR)
- **Knowledge Representation**: Encapsulates real-time telemetry facts (e.g., temperature, battery percentage, storage capacity, charger state).
- **IF-THEN Rules**: Evaluates condition-action rules for:
  - Overheating protection (cooling mode & screen dimming).
  - Low battery management (enabling Battery Saver mode).
  - Storage thresholds (cache cleanup prompts).
- **Inference Engine**: Sequentially executes rules against current facts to trigger automated system actions.

### Part 3: Case-Based Reasoning (CBR)
Demonstrates the **4 R's of CBR** for complex problem solving:
1. **Retrieve**: Compares new diagnostic issues against past cases using feature similarity scoring.
2. **Reuse**: Extracts the past solution from the highest-matching case.
3. **Revise**: Tailors the retrieved solution to fit the exact context of the new problem.
4. **Retain**: Learns by storing the new issue and its revised solution into the knowledge base for future queries.

---

## Repository Structure

.
├── Technical4.py   # Main Python script with RBR and CBR logic
└── README.md       # Project documentation

---

## Requirements

- **Python 3.x** (Uses standard Python data types; no third-party package dependencies required).

---

## How to Run

Run the script from your terminal:

```bash
python Technical4.py