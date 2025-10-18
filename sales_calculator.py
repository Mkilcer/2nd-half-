"""
CSV Sales Revenue Calculator

This program reads a CSV file containing sales data and calculates
the total sales revenue for a specific product.
"""

import csv
import sys
from typing import List, Dict, Optional


def read_csv_file(filename: str) -> List[Dict[str, str]]:
    """
    Read a CSV file and return the data as a list of dictionaries.
    
    Args:
        filename: Path to the CSV file
        
    Returns:
        List of dictionaries where each dictionary represents a row
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the CSV file is empty or malformed
    """
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
            
            if not data:
                raise ValueError("CSV file is empty or has no data rows")
                
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found")
    except csv.Error as e:
        raise ValueError(f"Error reading CSV file: {e}")


def calculate_product_revenue(data: List[Dict[str, str]], product_name: str, 
                               product_column: str = 'product',
                               quantity_column: str = 'quantity',
                               price_column: str = 'price') -> float:
    """
    Calculate the total sales revenue for a specific product.
    
    Args:
        data: List of dictionaries containing sales data
        product_name: Name of the product to calculate revenue for
        product_column: Name of the column containing product names (default: 'product')
        quantity_column: Name of the column containing quantities (default: 'quantity')
        price_column: Name of the column containing prices (default: 'price')
        
    Returns:
        Total revenue for the specified product
        
    Raises:
        ValueError: If required columns are missing or data is invalid
    """
    if not data:
        return 0.0
    
    # Check if required columns exist
    first_row = data[0]
    if product_column not in first_row:
        raise ValueError(f"Column '{product_column}' not found in CSV")
    if quantity_column not in first_row:
        raise ValueError(f"Column '{quantity_column}' not found in CSV")
    if price_column not in first_row:
        raise ValueError(f"Column '{price_column}' not found in CSV")
    
    total_revenue = 0.0
    
    for row in data:
        if row.get(product_column, '').strip().lower() == product_name.strip().lower():
            try:
                quantity = float(row.get(quantity_column, 0))
                price = float(row.get(price_column, 0))
                total_revenue += quantity * price
            except ValueError as e:
                print(f"Warning: Skipping invalid data in row: {row}. Error: {e}", 
                      file=sys.stderr)
                continue
    
    return total_revenue


def main():
    """
    Main function to run the sales revenue calculator from command line.
    """
    if len(sys.argv) < 3:
        print("Usage: python sales_calculator.py <csv_file> <product_name> [product_column] [quantity_column] [price_column]")
        print("\nExample: python sales_calculator.py sales.csv Laptop")
        print("Example: python sales_calculator.py sales.csv Laptop product qty unit_price")
        sys.exit(1)
    
    filename = sys.argv[1]
    product_name = sys.argv[2]
    
    # Optional column names
    product_column = sys.argv[3] if len(sys.argv) > 3 else 'product'
    quantity_column = sys.argv[4] if len(sys.argv) > 4 else 'quantity'
    price_column = sys.argv[5] if len(sys.argv) > 5 else 'price'
    
    try:
        # Read the CSV file
        data = read_csv_file(filename)
        
        # Calculate revenue
        revenue = calculate_product_revenue(
            data, 
            product_name,
            product_column,
            quantity_column,
            price_column
        )
        
        # Display results
        print(f"Total sales revenue for '{product_name}': ${revenue:.2f}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
