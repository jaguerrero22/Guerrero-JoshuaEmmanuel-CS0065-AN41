# TA4: Rule-Based and Case-Based Reasoning

## Overview

This program demonstrates two AI reasoning methods: Rule-Based Reasoning (RBR) and Case-Based Reasoning (CBR).

## Rule-Based Reasoning

The program checks preset facts about the environment and prints an action when a rule's condition is met:

- If the temperature is above 30°C and a user is present, turn on the air conditioner.
- If it is raining, bring an umbrella.
- If the humidity is above 80%, turn on the dehumidifier.

## Case-Based Reasoning

The program uses sample appliance problems to demonstrate the CBR cycle:

1. **Retrieve and Reuse** – Finds the most similar previous problem and uses its solution.
2. **Revise** – Applies a manual adjustment to the proposed solution.
3. **Retain** – Adds the new problem and final solution to the case base.

## How to Run

Requires Python 3. No external packages are needed.

From the repository's main folder, run:

```bash
python "Technical 4/Guerrero&Villaraza_Technical 4.py"
