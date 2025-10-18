"""
Question 4: Find Duplicates
Write a function that finds all duplicate elements in an array.
Return a list of unique duplicate values.
"""

def find_duplicates(arr):
    """
    Find all duplicate elements in an array.
    
    Args:
        arr (list): List of elements
        
    Returns:
        list: Sorted list of unique duplicate values
    """
    seen = set()
    duplicates = set()
    
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return sorted(list(duplicates))

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 2, 4, 5, 1], [1, 2]),
        ([1, 1, 1, 2, 2, 3], [1, 2]),
        ([5, 4, 3, 2, 1], []),
        (["a", "b", "c", "a", "d", "b"], ["a", "b"]),
        ([], []),
    ]
    
    print("Question 4: Find Duplicates")
    print("-" * 40)
    all_passed = True
    
    for arr, expected in test_cases:
        result = find_duplicates(arr)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"{status}: find_duplicates({arr}) = {result}")
        if result != expected:
            all_passed = False
    
    print("-" * 40)
    if all_passed:
        print("All tests passed!")
        exit(0)
    else:
        print("Some tests failed!")
        exit(1)
