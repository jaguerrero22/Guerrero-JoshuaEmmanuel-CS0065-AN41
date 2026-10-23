# Technical 1: Random Walk Simulation

This program simulates agents moving randomly on a square grid. It uses AgentPy to define the agents and Matplotlib to animate and display their positions.

## What the Program Does

- Asks for the number of agents, grid size, and number of steps.
- Animates the agents as they move on the grid.
- Records and prints each agent's path.
- Displays a chart of the agents' final positions.
- Compares two scenarios: 5 agents for 20 steps and 20 agents for 50 steps.
- Includes an `AvoidWalker` option that prevents an agent from moving into a cell occupied by another agent. The program uses `RandomWalker` by default.

## Requirements

- Python 3
- AgentPy
- Matplotlib

Install the required packages:

```bash
python -m pip install agentpy matplotlib
