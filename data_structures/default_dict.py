from collections import defaultdict
from typing import Dict


# Define a factory function to provide default values (int, in this case).
def default_int() -> int:
    """This function will be used to provide default values for keys that don't exist in the dictionary."""
    return 0


# Create a defaultdict with the default_int factory function.
word_count: Dict[str, int] = defaultdict(default_int)


def count_words(text: str) -> Dict[str, int]:
    """
    Count the occurrences of each word in the given text.

    Args:
        text (str): The input text.

    Returns:
        Dict[str, int]: A dictionary where keys are words and values are word counts.
    """
    words = text.split()
    for word in words:
        word_count[word] += 1
    return word_count


# Example usage
text = "This is a sample text. This text is for demonstration purposes."
word_counts = count_words(text)
print(word_counts)
