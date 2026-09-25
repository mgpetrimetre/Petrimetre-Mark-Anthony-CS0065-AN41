# Machine Problem 1: Early Warning Tool 

## Overview
This project uses KNIME Analytics Platform to predict student risk status (`risk_status`) using academic data.


## Algorithms Used
- **Decision Tree** (`Decision Tree Learner` & `Predictor`)
- **Logistic Regression** (with `Normalizer`, `Learner`, & `Predictor`)
- **Random Forest** (`Random Forest Learner` & `Predictor`)
- Model performance is evaluated using `Scorer` nodes.

## Repository Contents
- **`Demo/DemoEarlyWarningTool.knwf`**: Exported KNIME workflow file.
- **`Demo/student_performance_knime.csv`**: Required dataset.
- **`Demo/20231000131_Machine Problem1.pdf`**: Screenshots of executed nodes, CSV configuration, and Scorer results.
- **`README.md`**: Project documentation and instructions.

## How to Run the Workflow
1. Open **KNIME Analytics Platform**.
2. Go to **File** > **Import KNIME Workflow...** and select `Demo/DemoEarlyWarningTool.knwf`.
3. Open the workflow and double-click the **CSV Reader** node.
4. Set the **Source** path to `student_performance_knime.csv` inside the `Demo` folder, then click **Apply** and **OK**.
5. Press **Shift + F7** to execute all nodes (all nodes should turn green).
6. Right-click any **Scorer** node and select **Open view** to view the confusion matrix and accuracy metrics.
