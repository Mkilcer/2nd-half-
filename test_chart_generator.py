#!/usr/bin/env python3
"""
Test script for CSV Chart Generator
"""

import os
import sys
import pandas as pd
from pathlib import Path

# Import the functions from csv_chart_generator
from csv_chart_generator import read_csv_file, generate_chart


def test_read_csv():
    """Test reading the sample CSV file."""
    print("Test 1: Reading CSV file...")
    df = read_csv_file('sample_data.csv')
    
    # Check if DataFrame is not empty
    assert len(df) > 0, "DataFrame should not be empty"
    
    # Check if expected columns exist
    expected_columns = ['Month', 'Sales', 'Expenses', 'Profit']
    for col in expected_columns:
        assert col in df.columns, f"Column '{col}' should exist in DataFrame"
    
    print("✓ CSV reading test passed!")
    return df


def test_generate_bar_chart(df):
    """Test generating a bar chart."""
    print("\nTest 2: Generating bar chart...")
    output_file = '/tmp/test_bar_chart.png'
    
    # Remove file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)
    
    generate_chart(df, output_file, 'bar', 'Test Bar Chart')
    
    # Check if file was created
    assert os.path.exists(output_file), f"Chart file '{output_file}' should be created"
    assert os.path.getsize(output_file) > 0, "Chart file should not be empty"
    
    print("✓ Bar chart generation test passed!")


def test_generate_line_chart(df):
    """Test generating a line chart."""
    print("\nTest 3: Generating line chart...")
    output_file = '/tmp/test_line_chart.png'
    
    # Remove file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)
    
    generate_chart(df, output_file, 'line', 'Test Line Chart')
    
    # Check if file was created
    assert os.path.exists(output_file), f"Chart file '{output_file}' should be created"
    assert os.path.getsize(output_file) > 0, "Chart file should not be empty"
    
    print("✓ Line chart generation test passed!")


def test_generate_pie_chart(df):
    """Test generating a pie chart."""
    print("\nTest 4: Generating pie chart...")
    output_file = '/tmp/test_pie_chart.png'
    
    # Remove file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)
    
    generate_chart(df, output_file, 'pie', 'Test Pie Chart')
    
    # Check if file was created
    assert os.path.exists(output_file), f"Chart file '{output_file}' should be created"
    assert os.path.getsize(output_file) > 0, "Chart file should not be empty"
    
    print("✓ Pie chart generation test passed!")


def main():
    """Run all tests."""
    print("=" * 60)
    print("Running CSV Chart Generator Tests")
    print("=" * 60)
    
    try:
        # Test CSV reading
        df = test_read_csv()
        
        # Test chart generation
        test_generate_bar_chart(df)
        test_generate_line_chart(df)
        test_generate_pie_chart(df)
        
        print("\n" + "=" * 60)
        print("All tests passed! ✓")
        print("=" * 60)
        return 0
        
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
