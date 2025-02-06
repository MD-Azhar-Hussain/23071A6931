from collections import Counter

def most_common_word(text):
    words = text.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]  # Returns the most common word and its count

# Example usage
text = "apple banana apple orange banana apple"
print("Most common word:", most_common_word(text))
