"""
Question 1: Palindrome Checker
Write a function that checks if a given string is a palindrome.
A palindrome is a word, phrase, number, or other sequence of characters 
that reads the same forward and backward (ignoring spaces and case).
"""

def is_palindrome(text):
    """
    Check if the given text is a palindrome.
    
    Args:
        text (str): The text to check
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase
    cleaned = ''.join(text.split()).lower()
    # Check if the string equals its reverse
    return cleaned == cleaned[::-1]

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("A man a plan a canal Panama", True),
        ("Was it a car or a cat I saw", True),
        ("python", False),
    ]
    
    print("Question 1: Palindrome Checker")
    print("-" * 40)
    all_passed = True
    
    for text, expected in test_cases:
        result = is_palindrome(text)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"{status}: is_palindrome('{text}') = {result}")
        if result != expected:
            all_passed = False
    
    print("-" * 40)
    if all_passed:
        print("All tests passed!")
        exit(0)
    else:
        print("Some tests failed!")
        exit(1)
