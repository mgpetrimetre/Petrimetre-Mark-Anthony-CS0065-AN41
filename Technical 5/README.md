# Python Sentiment Analysis Tools

Two lightweight Python scripts demonstrating different approaches to sentiment and tone analysis: a rule-based lexicon matcher and a batch polarity analyzer using `TextBlob`.

---

## Project Structure

```text
├── Technical5.py      # Batch sentiment polarity analyzer using TextBlob
├── Techincal5p2.py    # Rule-based tone analyzer using custom word lexicons
└── README.md
```

---

## Scripts Overview

### 1. `Technical5.py` — Batch Sentiment Polarity Analyzer
Analyzes a batch of 10 user-inputted sentences using the `TextBlob` library.
* **How it works:** Evaluates each sentence's polarity score from `-1.0` (negative) to `1.0` (positive) and classifies it as **Positive**, **Neutral**, or **Negative**.
* **Output:** Prints individual polarity scores per sentence followed by a final summary count.

### 2. `Techincal5p2.py` — Lexicon-Based Tone Analyzer
Evaluates the emotional tone of a single sentence using curated word sets based on the Hu & Liu Opinion Lexicon.
* **How it works:** Strips punctuation, converts words to lowercase, and counts matches against predefined `HAPPY_WORDS` and `SAD_WORDS` sets.
* **Output:** Displays the count of happy and sad words detected and classifies the overall tone as **Happy (Positive)**, **Sad (Negative)**, or **Neutral**.

---

## Setup & Installation

* **Python 3.9+**

`Techincal5p2.py` uses only Python's standard library (`re`), while `Technical5.py` requires `textblob`.

```bash
pip install textblob
```

---

## Usage

### Batch Polarity Analyzer
```bash
python Technical5.py
```

**Sample Output:**
```text
--- Sentiment Analysis Batch (10 Entries) ---

[1/10] Enter a sentence: I love working on Python projects!
 -> Sentiment: Positive (Polarity: 0.62)

[2/10] Enter a sentence: The weather is okay today.
 -> Sentiment: Positive (Polarity: 0.50)
...
===================================
SENTIMENT ANALYSIS SUMMARY
===================================
Positive  : 6
Neutral   : 2
Negative  : 2
```

### Lexicon Tone Analyzer
```bash
python Techincal5p2.py
```

**Sample Output:**
```text
Enter a sentence to analyze: I am thrilled and grateful for this wonderful opportunity!

Happy words : 3
Sad words   : 0
Analysis    : The tone of the sentence is Happy (Positive).
```