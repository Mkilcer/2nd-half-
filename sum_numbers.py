#!/usr/bin/env python3
"""
Function to calculate the sum of all numbers in a text file.
"""


def sum_numbers_from_file(filename):
    """
    Reads a text file containing numbers and returns their sum.
    
    Args:
        filename (str): Path to the text file containing numbers
        
    Returns:
        float: Sum of all numbers in the file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the file contains non-numeric values
    """
    total = 0
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        total += float(line)
                    except ValueError:
                        raise ValueError(f"Invalid number found in file: {line}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filename}")
    
    return total


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python sum_numbers.py <filename>")
        sys.exit(1)
    
    try:
        result = sum_numbers_from_file(sys.argv[1])
        print(f"Sum of all numbers: {result}")
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)
