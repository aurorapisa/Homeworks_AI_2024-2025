import string
import re

def count_words(text: str) -> dict:
    """
    Count frequency of each word in text
    Args:
        text: Input string
    Returns:
        Dictionary with word frequencies
    """
    # Remove punctuation and convert the text to lowercase
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()

    # Split the text into words
    words = text.split()

    word_count = len(words)

    # Calculate word frequencies
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    print(f"There are {word_count} words in the text which are: {words}.")
    return word_freq
    pass

def find_longest_word(text: str) -> str:
    """
    Find the longest word in text
    Args:
        text: Input string
    Returns:
        Longest word found
    """
    # Remove punctuation and convert the text to lowercase
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()

    # Split the text into words
    words = text.split()

    # Handle empty input
    if not words:
        return ""

    longest_word = max(words, key=len)
    print(f"The longest word in the text is '{longest_word}'.")

    return longest_word
    pass

def format_sentences(text: str) -> list:
    """
    Split text into sentences and capitalize the first letter of each.
    Args:
        text: Input string
    Returns:
        List of formatted sentences
    """
    sentences = re.split(r'[.!?]', text)

    formatted_sentences = [sentence.strip().capitalize() for sentence in sentences if sentence.strip()]

    print(f"There are {len(formatted_sentences)} sentences in the text.")
    return formatted_sentences
    pass