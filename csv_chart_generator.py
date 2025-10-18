#!/usr/bin/env python3
"""
CSV Chart Generator
This program reads a CSV file and generates a chart using matplotlib.
"""

import pandas as pd
import matplotlib.pyplot as plt
import argparse
import sys
from pathlib import Path


def read_csv_file(csv_file):
    """
    Read CSV file and return a pandas DataFrame.
    
    Args:
        csv_file (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: DataFrame containing the CSV data
    """
    try:
        df = pd.read_csv(csv_file)
        return df
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: File '{csv_file}' is empty.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)


def generate_chart(df, output_file='chart.png', chart_type='bar', title='Data Visualization'):
    """
    Generate a chart from the DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame containing the data
        output_file (str): Output file name for the chart
        chart_type (str): Type of chart (bar, line, scatter, pie)
        title (str): Title for the chart
    """
    plt.figure(figsize=(10, 6))
    
    # Get the first column as x-axis (usually labels or categories)
    x_column = df.columns[0]
    
    if chart_type == 'bar':
        # Plot all numeric columns as bars
        df.plot(x=x_column, kind='bar', figsize=(10, 6))
        plt.ylabel('Values')
    elif chart_type == 'line':
        # Plot all numeric columns as lines
        df.plot(x=x_column, kind='line', figsize=(10, 6), marker='o')
        plt.ylabel('Values')
    elif chart_type == 'scatter':
        # For scatter plot, use first two numeric columns
        numeric_cols = df.select_dtypes(include=['number']).columns
        if len(numeric_cols) >= 2:
            plt.scatter(df[numeric_cols[0]], df[numeric_cols[1]])
            plt.xlabel(numeric_cols[0])
            plt.ylabel(numeric_cols[1])
        else:
            print("Error: Scatter plot requires at least two numeric columns.")
            sys.exit(1)
    elif chart_type == 'pie':
        # For pie chart, use first numeric column
        numeric_cols = df.select_dtypes(include=['number']).columns
        if len(numeric_cols) >= 1:
            plt.pie(df[numeric_cols[0]], labels=df[x_column], autopct='%1.1f%%')
        else:
            print("Error: Pie chart requires at least one numeric column.")
            sys.exit(1)
    else:
        print(f"Error: Chart type '{chart_type}' is not supported.")
        print("Supported types: bar, line, scatter, pie")
        sys.exit(1)
    
    plt.title(title)
    plt.xlabel(x_column)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Save the chart
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Chart saved successfully to '{output_file}'")
    
    # Optionally show the chart
    # plt.show()


def main():
    """Main function to parse arguments and generate chart."""
    parser = argparse.ArgumentParser(
        description='Read a CSV file and generate a chart using matplotlib'
    )
    parser.add_argument(
        'csv_file',
        help='Path to the CSV file'
    )
    parser.add_argument(
        '-o', '--output',
        default='chart.png',
        help='Output file name (default: chart.png)'
    )
    parser.add_argument(
        '-t', '--type',
        choices=['bar', 'line', 'scatter', 'pie'],
        default='bar',
        help='Chart type (default: bar)'
    )
    parser.add_argument(
        '--title',
        default='Data Visualization',
        help='Chart title (default: Data Visualization)'
    )
    
    args = parser.parse_args()
    
    # Read CSV file
    print(f"Reading CSV file: {args.csv_file}")
    df = read_csv_file(args.csv_file)
    print(f"Successfully read {len(df)} rows and {len(df.columns)} columns")
    print(f"\nData preview:\n{df.head()}\n")
    
    # Generate chart
    print(f"Generating {args.type} chart...")
    generate_chart(df, args.output, args.type, args.title)


if __name__ == '__main__':
    main()
