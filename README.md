# 2nd-half - Coding Questions Test Suite

This repository contains 5 coding questions with automated testing via PowerShell.

## 📋 Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Repository Structure](#repository-structure)
- [Coding Questions](#coding-questions)
- [Running the Tests](#running-the-tests)
- [How the Code Was Created](#how-the-code-was-created)
- [Understanding Each Component](#understanding-each-component)

## 🎯 Overview

This project demonstrates 5 fundamental coding challenges that test various programming concepts:
1. **Palindrome Checker** - String manipulation and comparison
2. **FizzBuzz** - Conditional logic and loops
3. **Array Sum** - Recursion and nested data structures
4. **Find Duplicates** - Sets and data structure optimization
5. **String Reversal** - Array manipulation and string operations

Each question includes a complete solution with built-in test cases.

## ⚙️ Prerequisites

Before running the test suite, ensure you have:

1. **Python 3.x** installed
   - Download from: https://www.python.org/downloads/
   - Verify installation: `python --version`

2. **PowerShell** (Windows has it by default, macOS/Linux can install PowerShell Core)
   - Windows: Built-in (PowerShell 5.1+)
   - macOS/Linux: Install from https://github.com/PowerShell/PowerShell

## 📁 Repository Structure

```
2nd-half-/
├── README.md              # This file - Documentation
├── test-runner.ps1        # PowerShell script to run all tests
├── question1/
│   └── solution.py        # Palindrome Checker solution
├── question2/
│   └── solution.py        # FizzBuzz solution
├── question3/
│   └── solution.py        # Array Sum solution
├── question4/
│   └── solution.py        # Find Duplicates solution
└── question5/
    └── solution.py        # String Reversal solution
```

## 📝 Coding Questions

### Question 1: Palindrome Checker
**Objective**: Write a function that checks if a given string is a palindrome.

**Key Concepts**:
- String manipulation
- Case-insensitive comparison
- Ignoring whitespace

**Example**: "A man a plan a canal Panama" → True

### Question 2: FizzBuzz
**Objective**: Generate a sequence where multiples of 3 are "Fizz", multiples of 5 are "Buzz", and multiples of both are "FizzBuzz".

**Key Concepts**:
- Modulo operations
- Conditional logic
- List generation

**Example**: fizzbuzz(15) → ["1", "2", "Fizz", "4", "Buzz", ...]

### Question 3: Array Sum
**Objective**: Calculate the sum of all numbers in an array, including nested arrays.

**Key Concepts**:
- Recursion
- Type checking
- Nested data structures

**Example**: [1, [2, 3], 4] → 10

### Question 4: Find Duplicates
**Objective**: Find all duplicate elements in an array.

**Key Concepts**:
- Set operations
- Hash tables
- Duplicate detection

**Example**: [1, 2, 3, 2, 1] → [1, 2]

### Question 5: String Reversal
**Objective**: Reverse the order of words in a sentence.

**Key Concepts**:
- String splitting
- Array reversal
- String joining

**Example**: "Hello World" → "World Hello"

## 🚀 Running the Tests

### Option 1: Using PowerShell Script (Recommended)

1. **Open PowerShell** in the repository directory:
   ```powershell
   cd path/to/2nd-half-
   ```

2. **Run the test runner**:
   ```powershell
   .\test-runner.ps1
   ```

   The script will:
   - Check if Python is installed
   - Run all 5 coding questions
   - Display results for each question
   - Provide a summary of passed/failed tests

### Option 2: Running Individual Questions

To run a specific question manually:

```bash
# Navigate to the repository
cd path/to/2nd-half-

# Run a specific question
python question1/solution.py
python question2/solution.py
python question3/solution.py
python question4/solution.py
python question5/solution.py
```

### Expected Output

When running the test suite, you should see:
- ✓ Green checkmarks for passing tests
- ✗ Red X marks for failing tests
- A summary showing how many questions passed

Example output:
```
═══════════════════════════════════════════════════════════
Question 1 : Palindrome Checker
═══════════════════════════════════════════════════════════
✓ PASS: is_palindrome('racecar') = True
✓ PASS: is_palindrome('hello') = False
...
All tests passed!
```

## 🔨 How the Code Was Created

### Step 1: Planning the Questions
1. **Identified 5 fundamental coding concepts** to test
2. **Chose problems** that represent common interview questions
3. **Ensured variety** in problem types (strings, arrays, logic, recursion)

### Step 2: Creating the Directory Structure
```bash
# Created separate directories for each question
mkdir question1 question2 question3 question4 question5
```

### Step 3: Implementing Solutions
For each question, we created a Python file with:
1. **Documentation** - Clear problem statement at the top
2. **Solution Function** - Clean, readable implementation
3. **Test Cases** - Multiple test cases covering edge cases
4. **Test Runner** - Built-in test execution with pass/fail reporting

Example structure of each solution:
```python
"""
Problem statement explaining the question
"""

def solution_function(input):
    """
    Function documentation
    """
    # Implementation
    pass

if __name__ == "__main__":
    # Test cases
    test_cases = [...]
    
    # Run tests and report results
    for test in test_cases:
        # Validate and print results
        pass
```

### Step 4: Creating the PowerShell Test Runner

The `test-runner.ps1` script was designed with:

1. **Prerequisites Check**:
   ```powershell
   # Check if Python is installed
   Test-PythonInstalled function
   ```

2. **Test Execution**:
   ```powershell
   # Run each question and capture results
   Test-CodingQuestion function
   ```

3. **Results Reporting**:
   ```powershell
   # Display colorful output with pass/fail status
   Write-Success, Write-Failure functions
   ```

4. **Summary Generation**:
   ```powershell
   # Count passed tests and display summary
   Main function
   ```

### Step 5: Documentation
Created this comprehensive README with:
- Clear installation instructions
- Repository structure diagram
- Detailed explanation of each question
- Multiple ways to run the tests
- Step-by-step creation process

## 🎓 Understanding Each Component

### Python Solutions
Each Python solution follows best practices:
- **Type hints in docstrings** for clarity
- **Descriptive variable names** for readability
- **Efficient algorithms** for performance
- **Comprehensive test coverage** for reliability
- **Exit codes** (0 for success, 1 for failure) for script integration

### PowerShell Script
The test runner demonstrates:
- **Function-based architecture** for modularity
- **Error handling** with try-catch blocks
- **Colorful output** using Write-Host with colors
- **Exit codes** for CI/CD integration
- **Cross-platform compatibility** (works on Windows, macOS, Linux with PowerShell Core)

### Design Decisions

1. **Why Python?**
   - Easy to read and understand
   - Great for teaching algorithms
   - Cross-platform compatibility
   - Rich built-in data structures

2. **Why PowerShell?**
   - Native to Windows environments
   - Powerful scripting capabilities
   - Good for automation and CI/CD
   - Can be used cross-platform with PowerShell Core

3. **Why separate directories?**
   - Clear organization
   - Easy to add more questions
   - Scalable structure
   - Each question is self-contained

## 🧪 Testing Philosophy

Each solution includes:
- **Happy path tests** - Normal expected inputs
- **Edge cases** - Empty inputs, single elements
- **Boundary conditions** - Maximum/minimum values
- **Special cases** - Problem-specific scenarios

## 🔄 Extending the Test Suite

To add a new question:

1. Create a new directory: `question6/`
2. Add your solution: `question6/solution.py`
3. Follow the existing format with test cases
4. Update the `test-runner.ps1` to include the new question
5. Update this README with the new question details

## 📚 Learning Outcomes

By studying this repository, you will learn:
- How to structure a multi-question coding challenge
- How to write self-testing code
- How to create automated test runners
- How to document code effectively
- Best practices for Python and PowerShell

## 🤝 Contributing

Feel free to:
- Add more test cases to existing questions
- Optimize existing solutions
- Add new coding questions
- Improve documentation
- Fix bugs or issues

## 📄 License

This project is created for educational purposes.

---

**Created**: October 18, 2024  
**Purpose**: Demonstrate coding fundamentals with automated testing
