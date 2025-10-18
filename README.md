# 2nd-half-
oct18 second half

## JSON File Reader

This project provides a Python module for reading JSON files and extracting specific information from them.

### Features

- **Read JSON files**: Load and parse JSON files safely
- **Extract specific information**: Get data by key names
- **Navigate nested structures**: Access deeply nested data using dot notation
- **Filter lists**: Find items in arrays that match specific criteria
- **Recursive search**: Find all occurrences of a key throughout the JSON structure

### Installation

No external dependencies required. Uses only Python standard library.

### Usage

#### Basic Usage

```python
from json_reader import read_json_file, extract_specific_info

# Read a JSON file
data = read_json_file("sample_data.json")

# Extract a specific key
metadata = extract_specific_info(data, "metadata")

# Extract multiple keys
info = extract_specific_info(data, ["metadata", "users"])
```

#### Extract Nested Information

```python
from json_reader import extract_nested_info

# Access nested data using dot notation
version = extract_nested_info(data, "metadata.version")

# Access array elements by index
first_user = extract_nested_info(data, "users.0.name")
```

#### Filter Lists

```python
from json_reader import filter_list_by_criteria

# Filter users by city
sf_users = filter_list_by_criteria(data, "users", {"city": "San Francisco"})

# Filter by multiple criteria
young_sf_users = filter_list_by_criteria(
    data, 
    "users", 
    {"city": "San Francisco", "age": 25}
)
```

#### Recursive Key Search

```python
from json_reader import get_all_values_by_key

# Get all email addresses from anywhere in the JSON
emails = get_all_values_by_key(data, "email")
```

### Running the Example

```bash
python json_reader.py
```

This will demonstrate all the features using the sample_data.json file.

### Running Tests

```bash
python -m unittest test_json_reader.py
```

Or run with verbose output:

```bash
python -m unittest test_json_reader.py -v
```

### Sample Data Format

The `sample_data.json` file contains example data with users and metadata:

```json
{
  "users": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com",
      "age": 30,
      "city": "New York"
    }
  ],
  "metadata": {
    "version": "1.0",
    "created": "2025-10-18",
    "total_users": 3
  }
}
```

### API Reference

#### `read_json_file(file_path)`
Reads and parses a JSON file.

**Parameters:**
- `file_path` (str): Path to the JSON file

**Returns:** Parsed JSON data as a dictionary

**Raises:**
- `FileNotFoundError`: If file doesn't exist
- `json.JSONDecodeError`: If file contains invalid JSON

#### `extract_specific_info(data, keys)`
Extracts specific keys from JSON data.

**Parameters:**
- `data` (dict): JSON data
- `keys` (str or list): Single key or list of keys to extract

**Returns:** Extracted data (value or dictionary)

#### `extract_nested_info(data, path)`
Extracts data from nested structures using dot notation.

**Parameters:**
- `data` (dict): JSON data
- `path` (str): Dot-separated path (e.g., "metadata.version" or "users.0.name")

**Returns:** Value at the specified path or None if not found

#### `filter_list_by_criteria(data, list_key, criteria)`
Filters a list based on matching criteria.

**Parameters:**
- `data` (dict): JSON data
- `list_key` (str): Key containing the list to filter
- `criteria` (dict): Key-value pairs to match

**Returns:** List of matching items

#### `get_all_values_by_key(data, target_key)`
Recursively finds all values for a specific key.

**Parameters:**
- `data`: JSON data (any type)
- `target_key` (str): Key to search for

**Returns:** List of all values found for the key
