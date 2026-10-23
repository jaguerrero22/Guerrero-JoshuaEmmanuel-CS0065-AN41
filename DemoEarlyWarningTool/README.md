# Asynchronous Activity 1: Student Early Warning Tool Using KNIME

This repository contains the project files for **Asynchronous Activity 1**. The KNIME workflow uses academic performance data to predict student risk status.

## Files

- `DemoEarlyWarningTool.knwf` — exported KNIME workflow
- `student_performance_knime.csv` — dataset used by the workflow

## Algorithms

The workflow uses these algorithms:

- Decision Tree
- Logistic Regression
- Random Forest

## How to Run

1. Open **KNIME Analytics Platform**.
2. Import `DemoEarlyWarningTool.knwf`.
3. Configure the **CSV Reader** node to use `student_performance_knime.csv`.
4. Execute all nodes in the workflow.
5. Open the **Scorer** nodes to review the evaluation results.

## Author

**Joshua Emmanuel A. Guerrero**

## Course and Section

**CS0065 — AN41**
