# AgentPy Random Walk Agent Simulation

An agent-based modeling (ABM) simulation built using [AgentPy](https://agentpy.readthedocs.io/) and Matplotlib. It simulates grid-based random walking agents with support for movement bias (drift) and collision avoidance, along with spatial quadrant analysis and trajectory visualization.

---

## Features

- **Agent Movement Modes**:
  - **Standard Walk**: Uniform 2D grid random walk (equal probability across 4 directions).
  - **Right-Drift Walk**: Biased movement with a 55% probability of moving right.
- **Collision Avoidance**: Prevents multiple agents from occupying the same grid cell at the same time.
- **Boundary Clamping**: Restricts agent movement within the grid dimensions.
- **Quadrant Distribution Analysis**: Calculates and prints agent spatial distribution across four quadrants (Q1–Q4) at the end of the simulation.
- **Trajectory Plotting**: Uses Matplotlib to plot path histories, starting positions (squares), and ending positions (circles) for each agent.

---

## Repository Structure

.
├── Tech1.py      # Main Python script containing the AgentPy model, agents, and visualization logic
└── README.md     # Project documentation

---

## Requirements

Install the necessary dependencies before running:

```bash
pip install agentpy matplotlib