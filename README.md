# 2nd-half-
oct18 second half

## Sum Numbers from File

This repository contains a Python function that reads a text file containing numbers (one per line) and calculates their sum.

### Usage

#### As a Python Module
```python
from sum_numbers import sum_numbers_from_file

result = sum_numbers_from_file("numbers.txt")
print(f"Sum: {result}")
```

#### As a Command-Line Script
```bash
python3 sum_numbers.py numbers.txt
```

### File Format

The text file should contain one number per line:
```
10
20
30
5.5
15.5
```

- Supports integers and floating-point numbers
- Empty lines are automatically skipped
- Negative numbers are supported

### Testing

Run the test suite:
```bash
python3 test_sum_numbers.py
```

### Example

A sample `numbers.txt` file is included in the repository with the following numbers:
- 10, 20, 30, 5.5, 15.5, 100
- Sum: 181.0
