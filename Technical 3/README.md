# TA3: Case-Based Reasoning Demo

## Overview

This program demonstrates a simple Case-Based Reasoning (CBR) system using sample cases involving electronic transfers and digital evidence. It compares a predefined new case with past cases, then adapts a strategy from the most similar case.


## How It Works

The program follows the CBR cycle:

1. **Retrieve** – Ranks the past cases by similarity to the new case.
2. **Reuse** – Selects the strategy from the most similar case.
3. **Revise** – Adds details tailored to the new case.
4. **Retain** – Adds the new case to the case list for the current run.

The similarity score compares the offense, evidence, method, and victim type. Each attribute has a different weight.

## Running the Program

Requires Python 3. No external packages are needed.

From the repository's main folder, run:

```bash
python "Technical 3/Guerrero&Villaraza_Technical 3.py"
