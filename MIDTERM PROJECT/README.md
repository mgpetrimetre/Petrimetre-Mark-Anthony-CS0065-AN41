# Faculty Scheduling & Consultation Slot Predictor

This repository contains machine learning models, data processing notebooks, workflow files, and a Streamlit web application to predict the availability of faculty consultation slots based on scheduling parameters.

---

## Features

- Machine Learning Models: Predicts slot availability using Decision Tree Classifier and Logistic Regression.
- KNIME Workflow: Includes visual workflow assets for data processing, training, and evaluation.
- Python Notebooks: End-to-end data encoding, model evaluation (confusion matrix, classification reports), and feature importance visualization.
- Web Application: A Streamlit interface for checking slot availability in real time.

---

## Repository Structure

.
├── Faculty Scheduling1/         # KNIME Analytics Platform workflow configuration
├── faculty_consultations.csv   # Dataset containing schedule & consultation records
├── app.py                      # Streamlit web application
└── README.md                   # Project documentation

---

## Dataset Schema

The dataset (`faculty_consultations.csv`) includes the following fields:

- Faculty: Name of the faculty member
- Day: Day of the week
- TimeSlot: Start time of the consultation slot
- StudentYear: Year level of the student (1 to 4)
- Duration: Duration of the slot in minutes (15, 30, 60)
- CurrentBookings: Number of existing bookings for the slot
- SlotAvailable: Target column (Yes / No)

---

## Requirements

Install the necessary Python packages:

pip install pandas numpy scikit-learn matplotlib streamlit

---

## Usage

### Run Python Scripts/Notebooks
Train and evaluate the models using Python:

python -c "import pandas as pd; df = pd.read_csv('faculty_consultations.csv'); print(df.head())"

### Launch Streamlit Web App
To run the interactive slot checker:

streamlit run app.py

1. Open your browser at http://localhost:8501.
2. Upload `faculty_consultations.csv`.
3. Select slot parameters and click Check Availability.

---

## Model Performance

Evaluated test results:

- Decision Tree Classifier: ~83.33% Accuracy
- Logistic Regression: ~91.67% Accuracy

---

## Tech Stack

- Python (Pandas, NumPy, Scikit-learn, Matplotlib, Streamlit)
- KNIME Analytics Platform