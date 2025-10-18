"""
Question 5: String Reversal
Write a function that reverses the order of words in a sentence.
The words themselves should remain intact, but their order should be reversed.
"""

def reverse_words(sentence):
    """
    Reverse the order of words in a sentence.
    
    Args:
        sentence (str): The input sentence
        
    Returns:
        str: Sentence with words in reversed order
    """
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("Hello World", "World Hello"),
        ("The quick brown fox", "fox brown quick The"),
        ("Python", "Python"),
        ("one two three four five", "five four three two one"),
        ("", ""),
    ]
    
    print("Question 5: String Reversal")
    print("-" * 40)
    all_passed = True
    
    for sentence, expected in test_cases:
        result = reverse_words(sentence)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"{status}: reverse_words('{sentence}') = '{result}'")
        if result != expected:
            all_passed = False
    
    print("-" * 40)
    if all_passed:
        print("All tests passed!")
        exit(0)
    else:
        print("Some tests failed!")
        exit(1)
