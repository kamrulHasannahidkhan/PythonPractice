import re

def find_longest_word(sentence: str) -> str:
    words = re.findall(r'\b\w+\b', sentence)
    if not words:
        return ""
    return max(words, key=len)

# Example Usage
print(find_longest_word("The quick brown fox jumped over the lazy dog"))  # Output: jumped