# Rule-Based Vacuum Cleaner Agent Simulation

A simple Python implementation of a two-room rule-based vacuum cleaner agent. The agent perceives its current room's cleanliness state and performs simple condition-action rules to clean rooms and navigate between them.

---

## Features

- **Rule-Based Perception & Action**:
  - If the current room is **Dirty**, the agent cleans it.
  - If the current room is **Clean**, the agent moves to the other room.
- **Interactive Simulation**: Prompt-based terminal interface to configure initial room conditions, starting room, and execution step count.
- **Step-by-Step Logging**: Tracks and prints the agent's location, actions, and environment state at every step.

---

## Repository Structure

.
├── Tech2.py      # Main Python script for the agent and simulation loop
└── README.md     # Project documentation

---

## How It Works

1. The environment consists of two rooms: **Room A** and **Room B**.
2. Room states can be either `Clean` or `Dirty`.
3. The agent evaluates its location at each step:
   - **Dirty** -> Action: `Cleaned room [X]` (changes room state to `Clean`).
   - **Clean** -> Action: `Moved from Room [X] to Room [Y]` (switches current room).

---

## Requirements

- Python 3.x (Uses built-in libraries only; no third-party package dependencies required).

---

## Usage

Run the Python script directly in your terminal:

```bash
python Tech2.py