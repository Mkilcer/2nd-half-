# 2nd-half-
oct18 second half

## CSV Sales Revenue Calculator

A Python program that reads a CSV file and calculates the total sales revenue for a specific product.

### Features
- Read sales data from CSV files
- Calculate total revenue for any product
- Case-insensitive product name matching
- Support for custom column names
- Comprehensive error handling
- Extensive unit tests

### Usage

#### Command Line
```bash
python sales_calculator.py <csv_file> <product_name> [product_column] [quantity_column] [price_column]
```

**Examples:**
```bash
# Basic usage with default column names (product, quantity, price)
python sales_calculator.py sales_data.csv Laptop

# Case-insensitive product name
python sales_calculator.py sales_data.csv LAPTOP

# Custom column names
python sales_calculator.py custom_data.csv Laptop item qty unit_price
```

#### As a Module
```python
from sales_calculator import read_csv_file, calculate_product_revenue

# Read CSV file
data = read_csv_file('sales_data.csv')

# Calculate revenue for a specific product
revenue = calculate_product_revenue(data, 'Laptop')
print(f"Total revenue: ${revenue:.2f}")
```

### CSV File Format

The CSV file should have the following default columns:
- `product`: Name of the product
- `quantity`: Number of units sold
- `price`: Price per unit

**Example CSV:**
```csv
product,quantity,price
Laptop,2,999.99
Mouse,5,25.50
Keyboard,3,75.00
```

You can use custom column names by specifying them as command-line arguments.

### Testing

Run the unit tests:
```bash
python -m unittest test_sales_calculator.py -v
```

### Sample Data

A sample CSV file (`sales_data.csv`) is included with example sales data for:
- Laptops
- Mice
- Keyboards
- Monitors
- Headphones

### Error Handling

The program handles various error scenarios:
- File not found
- Empty CSV files
- Missing required columns
- Invalid numeric data (skips invalid rows with a warning)
- Malformed CSV files
