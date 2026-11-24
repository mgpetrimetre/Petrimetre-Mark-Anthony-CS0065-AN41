from collections import Counter
from textblob import TextBlob


def classify_polarity(polarity: float) -> str:
    """Categorizes a TextBlob polarity score into a sentiment label."""
    if polarity < 0:
        return "Negative"
    elif polarity == 0:
        return "Neutral"
    return "Positive"


def run_batch_analysis(iterations: int = 10) -> None:
    """Prompts the user for sentences and summarizes sentiment distribution."""
    results = Counter()

    print(f"--- Sentiment Analysis Batch ({iterations} Entries) ---\n")

    for i in range(1, iterations + 1):
        while True:
            sentence = input(f"[{i}/{iterations}] Enter a sentence: ").strip()
            if sentence:
                break
            print("Input cannot be empty. Please try again.")

        blob = TextBlob(sentence)
        polarity = blob.sentiment.polarity
        sentiment = classify_polarity(polarity)

        results[sentiment] += 1
        print(f" -> Sentiment: {sentiment} (Polarity: {polarity:.2f})\n")

    print("=" * 35)
    print("SENTIMENT ANALYSIS SUMMARY")
    print("=" * 35)
    for label in ("Positive", "Neutral", "Negative"):
        print(f"{label:<10}: {results[label]}")


if __name__ == "__main__":
    run_batch_analysis(10)