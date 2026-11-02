import re
from pathlib import Path

DATA_FOLDER = Path(__file__).resolve().parent / "data"


def load_words(filename):
    # The dataset uses Latin-1; semicolon lines are comments.
    with (DATA_FOLDER / filename).open(encoding="latin-1") as file:
        return {line.strip().lower() for line in file
                if line.strip() and not line.startswith(";")}


HAPPY_WORDS = load_words("positive-words.txt")
SAD_WORDS = load_words("negative-words.txt")


def words_in(sentence):
    # Ignore case and punctuation; keep internal hyphens/apostrophes.
    return re.findall(r"[a-z0-9]+(?:[-'][a-z0-9]+)*(?:\+)?",
                      sentence.lower().replace("\u2019", "'"))


def number_happy(sentence):
    return sum(word in HAPPY_WORDS for word in words_in(sentence))


def number_sad(sentence):
    return sum(word in SAD_WORDS for word in words_in(sentence))


def main():
    sentence = input("Enter a sentence: ").strip()
    while not sentence:
        sentence = input("Please enter a non-empty sentence: ").strip()

    happy = number_happy(sentence)
    sad = number_sad(sentence)
    print(f"Happy words: {happy}")
    print(f"Sad words: {sad}")

    if happy > sad:
        print("Analysis: Positive (happy)")
    elif sad > happy:
        print("Analysis: Negative (sad)")
    else:
        print("Analysis: Neutral")


if __name__ == "__main__":
    main()
