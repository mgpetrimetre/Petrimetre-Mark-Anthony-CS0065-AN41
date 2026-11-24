import re

# Curated subset based on the Hu & Liu Opinion Lexicon (Public Sentiment Dataset)
HAPPY_WORDS = {
    "amazing", "awesome", "bliss", "bright", "brilliant", "cheerful",
    "delighted", "ecstatic", "elated", "excellent", "excited", "fantastic",
    "glad", "good", "grateful", "great", "happy", "harmonious", "hopeful",
    "inspired", "joy", "joyful", "jubilant", "kind", "lively", "love",
    "lovely", "marvelous", "optimistic", "outstanding", "peaceful", "pleasant",
    "pleased", "positive", "proud", "radiant", "relieved", "remarkable",
    "satisfied", "smiling", "splendid", "successful", "superb", "terrific",
    "thankful", "thrilled", "triumph", "upbeat", "vibrant", "wonderful"
}

SAD_WORDS = {
    "abandoned", "agonizing", "alone", "angry", "anxious", "awful", "bad",
    "bitter", "bleak", "broken", "crushed", "crying", "defeated", "dejected",
    "depressed", "despair", "devastated", "disappointed", "dismal", "distressed",
    "downcast", "dreadful", "empty", "failure", "fearful", "frustrated",
    "gloomy", "grief", "grim", "guilty", "heartbroken", "helpless", "hopeless",
    "hurt", "isolated", "lonely", "melancholy", "miserable", "mournful",
    "negative", "pain", "pathetic", "pessimistic", "regret", "rejected",
    "sad", "sorrow", "suffer", "terrible", "tragic", "unhappy", "upset", "woeful"
}


def tokenize(text: str) -> list[str]:
    """Extracts lowercase alphabetic words, stripping punctuation."""
    return re.findall(r"\b[a-z]+\b", text.lower())


def number_happy(sentence: str) -> int:
    """Returns the count of happy words present in the given sentence."""
    words = tokenize(sentence)
    return sum(1 for word in words if word in HAPPY_WORDS)


def number_sad(sentence: str) -> int:
    """Returns the count of sad words present in the given sentence."""
    words = tokenize(sentence)
    return sum(1 for word in words if word in SAD_WORDS)


def analyze_tone(sentence: str) -> None:
    """Evaluates and prints the happy/sad word counts and overall tone."""
    happy_count = number_happy(sentence)
    sad_count = number_sad(sentence)

    if happy_count > sad_count:
        tone = "Happy"
        analysis = "Positive"
    elif sad_count > happy_count:
        tone = "Sad"
        analysis = "Negative"
    else:
        tone = "Neutral"
        analysis = "Neutral"

    print(f"\nHappy words : {happy_count}")
    print(f"Sad words   : {sad_count}")
    print(f"Analysis    : The tone of the sentence is {tone} ({analysis}).")


if __name__ == "__main__":
    user_sentence = input("Enter a sentence to analyze: ")
    analyze_tone(user_sentence)