"""
Unit tests for the sales_calculator module
"""

import unittest
import os
import csv
import tempfile
from sales_calculator import read_csv_file, calculate_product_revenue


class TestSalesCalculator(unittest.TestCase):
    """Test cases for the sales calculator functions"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_data = [
            {'product': 'Laptop', 'quantity': '2', 'price': '999.99'},
            {'product': 'Mouse', 'quantity': '5', 'price': '25.50'},
            {'product': 'Laptop', 'quantity': '1', 'price': '999.99'},
            {'product': 'Keyboard', 'quantity': '3', 'price': '75.00'},
            {'product': 'Mouse', 'quantity': '10', 'price': '25.50'},
        ]
        
    def test_calculate_product_revenue_laptop(self):
        """Test calculating revenue for Laptop"""
        # Expected: (2 * 999.99) + (1 * 999.99) = 2999.97
        revenue = calculate_product_revenue(self.test_data, 'Laptop')
        self.assertAlmostEqual(revenue, 2999.97, places=2)
    
    def test_calculate_product_revenue_mouse(self):
        """Test calculating revenue for Mouse"""
        # Expected: (5 * 25.50) + (10 * 25.50) = 382.50
        revenue = calculate_product_revenue(self.test_data, 'Mouse')
        self.assertAlmostEqual(revenue, 382.50, places=2)
    
    def test_calculate_product_revenue_keyboard(self):
        """Test calculating revenue for Keyboard"""
        # Expected: 3 * 75.00 = 225.00
        revenue = calculate_product_revenue(self.test_data, 'Keyboard')
        self.assertAlmostEqual(revenue, 225.00, places=2)
    
    def test_calculate_product_revenue_nonexistent(self):
        """Test calculating revenue for non-existent product"""
        revenue = calculate_product_revenue(self.test_data, 'NonExistent')
        self.assertEqual(revenue, 0.0)
    
    def test_calculate_product_revenue_case_insensitive(self):
        """Test that product name matching is case-insensitive"""
        revenue = calculate_product_revenue(self.test_data, 'LAPTOP')
        self.assertAlmostEqual(revenue, 2999.97, places=2)
    
    def test_calculate_product_revenue_empty_data(self):
        """Test with empty data list"""
        revenue = calculate_product_revenue([], 'Laptop')
        self.assertEqual(revenue, 0.0)
    
    def test_calculate_product_revenue_custom_columns(self):
        """Test with custom column names"""
        custom_data = [
            {'item': 'Laptop', 'qty': '2', 'unit_price': '999.99'},
            {'item': 'Mouse', 'qty': '5', 'unit_price': '25.50'},
        ]
        revenue = calculate_product_revenue(
            custom_data, 'Laptop', 
            product_column='item',
            quantity_column='qty',
            price_column='unit_price'
        )
        self.assertAlmostEqual(revenue, 1999.98, places=2)
    
    def test_calculate_product_revenue_missing_column(self):
        """Test error handling when required column is missing"""
        with self.assertRaises(ValueError):
            calculate_product_revenue(self.test_data, 'Laptop', product_column='invalid')
    
    def test_read_csv_file(self):
        """Test reading a CSV file"""
        # Create a temporary CSV file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['product', 'quantity', 'price'])
            writer.writeheader()
            writer.writerows(self.test_data)
            temp_filename = f.name
        
        try:
            # Read the file
            data = read_csv_file(temp_filename)
            self.assertEqual(len(data), 5)
            self.assertEqual(data[0]['product'], 'Laptop')
            self.assertEqual(data[1]['product'], 'Mouse')
        finally:
            # Clean up
            os.unlink(temp_filename)
    
    def test_read_csv_file_not_found(self):
        """Test error handling when file doesn't exist"""
        with self.assertRaises(FileNotFoundError):
            read_csv_file('nonexistent_file.csv')
    
    def test_read_csv_file_empty(self):
        """Test error handling when CSV file is empty"""
        # Create a temporary empty CSV file (with header only)
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['product', 'quantity', 'price'])
            writer.writeheader()
            temp_filename = f.name
        
        try:
            with self.assertRaises(ValueError):
                read_csv_file(temp_filename)
        finally:
            os.unlink(temp_filename)
    
    def test_calculate_with_invalid_numeric_data(self):
        """Test handling of invalid numeric data"""
        invalid_data = [
            {'product': 'Laptop', 'quantity': 'invalid', 'price': '999.99'},
            {'product': 'Laptop', 'quantity': '2', 'price': '999.99'},
        ]
        # Should skip invalid row and calculate only valid one
        revenue = calculate_product_revenue(invalid_data, 'Laptop')
        self.assertAlmostEqual(revenue, 1999.98, places=2)


class TestIntegration(unittest.TestCase):
    """Integration tests using the actual sample CSV file"""
    
    def test_with_sample_file(self):
        """Test with the provided sales_data.csv file"""
        csv_file = '/home/runner/work/2nd-half-/2nd-half-/sales_data.csv'
        
        # Skip if file doesn't exist
        if not os.path.exists(csv_file):
            self.skipTest("sales_data.csv not found")
        
        data = read_csv_file(csv_file)
        
        # Test Laptop: 2*999.99 + 1*999.99 + 3*999.99 = 5999.94
        laptop_revenue = calculate_product_revenue(data, 'Laptop')
        self.assertAlmostEqual(laptop_revenue, 5999.94, places=2)
        
        # Test Mouse: 5*25.50 + 10*25.50 + 2*25.50 = 433.50
        mouse_revenue = calculate_product_revenue(data, 'Mouse')
        self.assertAlmostEqual(mouse_revenue, 433.50, places=2)
        
        # Test Keyboard: 3*75.00 + 1*75.00 = 300.00
        keyboard_revenue = calculate_product_revenue(data, 'Keyboard')
        self.assertAlmostEqual(keyboard_revenue, 300.00, places=2)


if __name__ == '__main__':
    unittest.main()
