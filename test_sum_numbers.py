#!/usr/bin/env python3
"""
Tests for the sum_numbers_from_file function.
"""

import unittest
import os
import tempfile
from sum_numbers import sum_numbers_from_file


class TestSumNumbers(unittest.TestCase):
    
    def test_sum_positive_integers(self):
        """Test summing positive integers from file"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("10\n20\n30\n")
            temp_file = f.name
        
        try:
            result = sum_numbers_from_file(temp_file)
            self.assertEqual(result, 60)
        finally:
            os.unlink(temp_file)
    
    def test_sum_with_decimals(self):
        """Test summing decimal numbers from file"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("10.5\n20.5\n5\n")
            temp_file = f.name
        
        try:
            result = sum_numbers_from_file(temp_file)
            self.assertEqual(result, 36.0)
        finally:
            os.unlink(temp_file)
    
    def test_sum_with_negative_numbers(self):
        """Test summing negative numbers from file"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("10\n-5\n20\n-10\n")
            temp_file = f.name
        
        try:
            result = sum_numbers_from_file(temp_file)
            self.assertEqual(result, 15)
        finally:
            os.unlink(temp_file)
    
    def test_sum_with_empty_lines(self):
        """Test that empty lines are skipped"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("10\n\n20\n\n30\n")
            temp_file = f.name
        
        try:
            result = sum_numbers_from_file(temp_file)
            self.assertEqual(result, 60)
        finally:
            os.unlink(temp_file)
    
    def test_file_not_found(self):
        """Test that FileNotFoundError is raised for non-existent file"""
        with self.assertRaises(FileNotFoundError):
            sum_numbers_from_file("non_existent_file.txt")
    
    def test_invalid_number(self):
        """Test that ValueError is raised for non-numeric content"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("10\nabc\n20\n")
            temp_file = f.name
        
        try:
            with self.assertRaises(ValueError):
                sum_numbers_from_file(temp_file)
        finally:
            os.unlink(temp_file)
    
    def test_sample_numbers_file(self):
        """Test with the included numbers.txt sample file"""
        # Expected: 10 + 20 + 30 + 5.5 + 15.5 + 100 = 181
        result = sum_numbers_from_file("numbers.txt")
        self.assertEqual(result, 181.0)


if __name__ == '__main__':
    unittest.main()
