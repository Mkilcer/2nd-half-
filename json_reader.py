"""
JSON Reader Module

This module provides functionality to read JSON files and extract specific information.
"""

import json
import os


def read_json_file(file_path):
    """
    Read a JSON file and return its contents.
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        dict: Parsed JSON data
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    return data


def extract_specific_info(data, keys):
    """
    Extract specific information from JSON data based on provided keys.
    
    Args:
        data (dict): JSON data (dictionary)
        keys (list or str): Single key or list of keys to extract
        
    Returns:
        dict or any: Extracted data. Returns a dictionary if multiple keys,
                     or the value if a single key is provided
    """
    if isinstance(keys, str):
        # Single key provided
        return data.get(keys)
    
    # Multiple keys provided
    result = {}
    for key in keys:
        if key in data:
            result[key] = data[key]
    
    return result


def extract_nested_info(data, path):
    """
    Extract information from nested JSON structure using a path.
    
    Args:
        data (dict): JSON data
        path (str): Dot-separated path to the value (e.g., "metadata.version")
        
    Returns:
        any: Value at the specified path, or None if not found
    """
    keys = path.split('.')
    current = data
    
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, list):
            try:
                index = int(key)
                current = current[index]
            except (ValueError, IndexError):
                return None
        else:
            return None
    
    return current


def filter_list_by_criteria(data, list_key, criteria):
    """
    Filter a list in JSON data based on specific criteria.
    
    Args:
        data (dict): JSON data
        list_key (str): Key that contains the list to filter
        criteria (dict): Dictionary of key-value pairs to match
        
    Returns:
        list: Filtered list of items matching the criteria
    """
    if list_key not in data or not isinstance(data[list_key], list):
        return []
    
    filtered = []
    for item in data[list_key]:
        match = True
        for key, value in criteria.items():
            if key not in item or item[key] != value:
                match = False
                break
        if match:
            filtered.append(item)
    
    return filtered


def get_all_values_by_key(data, target_key):
    """
    Recursively extract all values for a specific key from JSON data.
    
    Args:
        data: JSON data (can be dict, list, or any type)
        target_key (str): The key to search for
        
    Returns:
        list: All values found for the target key
    """
    results = []
    
    def recursive_search(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == target_key:
                    results.append(value)
                recursive_search(value)
        elif isinstance(obj, list):
            for item in obj:
                recursive_search(item)
    
    recursive_search(data)
    return results


if __name__ == "__main__":
    # Example usage
    try:
        # Read the sample JSON file
        data = read_json_file("sample_data.json")
        print("Full JSON data:")
        print(json.dumps(data, indent=2))
        print("\n" + "="*50 + "\n")
        
        # Extract specific top-level keys
        metadata = extract_specific_info(data, "metadata")
        print("Metadata:")
        print(json.dumps(metadata, indent=2))
        print("\n" + "="*50 + "\n")
        
        # Extract multiple keys
        info = extract_specific_info(data, ["metadata", "users"])
        print("Extracted metadata and users:")
        print(f"Number of keys extracted: {len(info)}")
        print("\n" + "="*50 + "\n")
        
        # Extract nested information
        version = extract_nested_info(data, "metadata.version")
        print(f"Version: {version}")
        
        first_user_name = extract_nested_info(data, "users.0.name")
        print(f"First user name: {first_user_name}")
        print("\n" + "="*50 + "\n")
        
        # Filter users by city
        sf_users = filter_list_by_criteria(data, "users", {"city": "San Francisco"})
        print("Users in San Francisco:")
        print(json.dumps(sf_users, indent=2))
        print("\n" + "="*50 + "\n")
        
        # Get all email addresses
        emails = get_all_values_by_key(data, "email")
        print("All email addresses:")
        for email in emails:
            print(f"  - {email}")
        
    except Exception as e:
        print(f"Error: {e}")
