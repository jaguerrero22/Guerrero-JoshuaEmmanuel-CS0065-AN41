from textblob import TextBlob


def main():
    positive = 0
    neutral = 0
    negative = 0

    for number in range(1, 11):
        sentence = input(f"Enter sentence {number}/10: ").strip()
        while not sentence:
            sentence = input("Please enter a non-empty sentence: ").strip()

        polarity = TextBlob(sentence).sentiment.polarity
        if polarity < 0:
            print("Negative")
            negative += 1
        elif polarity == 0:
            print("Neutral")
            neutral += 1
        else:
            print("Positive")
            positive += 1

    print("\nSummary of 10 sentences")
    print(f"Positive: {positive}")
    print(f"Neutral: {neutral}")
    print(f"Negative: {negative}")


if __name__ == "__main__":
    main()