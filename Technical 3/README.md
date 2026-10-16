# CBR Intelligent Tutoring System: Mandarin Chinese

An interactive Python application that uses **Case-Based Reasoning (CBR)** to diagnose Mandarin Chinese learning difficulties and provide personalized instructional feedback and practice recommendations.

---

Case-Based Reasoning solves new problems by retrieving and adapting solutions from a database of past experiences. This system applies the **4 R's of CBR**:

1. **Retrieve**: Searches the case base for the most similar past student issue using weighted similarity matching (error pattern > topic > proficiency level).
2. **Reuse**: Extracts the past instructional feedback and practice item count.
3. **Revise (Adapt)**: Tailors the solution based on specific student profile needs (e.g., adding extra practice and foundational instructions for `absolute_beginner` learners).
4. **Retain**: Automatically saves the newly solved problem and its adapted solution into the active case base for future learning.

---

## Features

- **Initial Knowledge Base**: Pre-loaded with common Mandarin learning issues covering tones, stroke order, pinyin pronunciation, measure words, and character recognition.
- **Weighted Similarity Matching**: Prioritizes matching specific error patterns over broad topics and levels.
- **Dynamic Case Learning**: Appends new cases into memory during the execution loop, expanding system intelligence over time.
- **Interactive CLI**: Easy-to-use terminal interface for entering new student problems.

---

## Repository Structure

.
├── Technical3.py   # Main Python script containing CBR logic and interactive loop
└── README.md       # Project documentation

---

## Requirements

- **Python 3.x** (Uses built-in libraries only; no external package dependencies needed).

---

## How to Run

Execute the script from your terminal:

```bash
python Technical3.py