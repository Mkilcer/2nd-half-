"""
Question 3: Array Sum
Write a function that calculates the sum of all numbers in an array,
including nested arrays.
"""

def array_sum(arr):
    """
    Calculate the sum of all numbers in an array (including nested arrays).
    
    Args:
        arr (list): List that may contain numbers and/or nested lists
        
    Returns:
        int/float: Sum of all numbers
    """
    total = 0
    for item in arr:
        if isinstance(item, list):
            total += array_sum(item)
        elif isinstance(item, (int, float)):
            total += item
    return total

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 15),
        ([1, [2, 3], 4, [5, 6]], 21),
        ([[1, 2], [3, 4], [5, 6]], 21),
        ([1, [2, [3, [4, 5]]]], 15),
        ([], 0),
    ]
    
    print("Question 3: Array Sum")
    print("-" * 40)
    all_passed = True
    
    for arr, expected in test_cases:
        result = array_sum(arr)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"{status}: array_sum({arr}) = {result}")
        if result != expected:
            all_passed = False
    
    print("-" * 40)
    if all_passed:
        print("All tests passed!")
        exit(0)
    else:
        print("Some tests failed!")
        exit(1)
