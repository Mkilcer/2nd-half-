# CSV Chart Generator

A Python program that reads CSV files and generates charts using matplotlib.

## Features

- Read CSV files and visualize data
- Support for multiple chart types: bar, line, scatter, and pie
- Customizable chart titles and output file names
- Easy-to-use command-line interface

## Requirements

- Python 3.6 or higher
- matplotlib
- pandas

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Mkilcer/2nd-half-.git
cd 2nd-half-
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python3 csv_chart_generator.py <csv_file>
```

With options:
```bash
python3 csv_chart_generator.py <csv_file> -o <output_file> -t <chart_type> --title "<chart_title>"
```

### Arguments

- `csv_file` (required): Path to the CSV file
- `-o, --output`: Output file name (default: chart.png)
- `-t, --type`: Chart type - bar, line, scatter, or pie (default: bar)
- `--title`: Chart title (default: Data Visualization)

### Examples

Generate a bar chart:
```bash
python3 csv_chart_generator.py sample_data.csv -o bar_chart.png -t bar --title "Monthly Sales Report"
```

Generate a line chart:
```bash
python3 csv_chart_generator.py sample_data.csv -o line_chart.png -t line --title "Monthly Trends"
```

Generate a pie chart:
```bash
python3 csv_chart_generator.py sample_data.csv -o pie_chart.png -t pie --title "Sales Distribution"
```

## Sample Data

A sample CSV file (`sample_data.csv`) is included in the repository with monthly sales data that you can use to test the program.

## CSV File Format

The CSV file should have:
- A header row with column names
- The first column typically contains labels/categories (e.g., months, names)
- Subsequent columns contain numeric data to be plotted

Example:
```csv
Month,Sales,Expenses,Profit
January,15000,8000,7000
February,18000,9000,9000
March,22000,10000,12000
```

## Output

The program generates a high-resolution PNG image (300 DPI) of the chart and saves it to the specified output file.
