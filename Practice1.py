def reverse_string(text: str) -> str:
    # Use Python's syntax for slicing: [start:stop:step]
    # A step of -1 walks through the string backwards
    return text[::-1]

# Test the function
print(reverse_string("hello"))  # Output: "olleh"