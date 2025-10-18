"""
Question 2: FizzBuzz
Write a function that returns a list of numbers from 1 to n, but:
- For multiples of 3, replace with "Fizz"
- For multiples of 5, replace with "Buzz"
- For multiples of both 3 and 5, replace with "FizzBuzz"
"""

def fizzbuzz(n):
    """
    Generate FizzBuzz sequence up to n.
    
    Args:
        n (int): The upper limit (inclusive)
        
    Returns:
        list: List of numbers/strings following FizzBuzz rules
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# Test cases
if __name__ == "__main__":
    print("Question 2: FizzBuzz")
    print("-" * 40)
    
    # Test case 1
    result = fizzbuzz(15)
    expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", 
                "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    
    test_passed = result == expected
    status = "✓ PASS" if test_passed else "✗ FAIL"
    print(f"{status}: fizzbuzz(15)")
    print(f"Result: {result[:5]}...{result[-3:]}")
    
    print("-" * 40)
    if test_passed:
        print("All tests passed!")
        exit(0)
    else:
        print("Some tests failed!")
        exit(1)
