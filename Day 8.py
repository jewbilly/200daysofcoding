def reverse_string(s):
    """
    Recursively reverse a string.
    Base case: if the string is empty or has one character, return it.
    """
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


# Example usage

original = "recursion"
reversed_str = reverse_string(original)

print("Original:", original)
print("Reversed:", reversed_str)
