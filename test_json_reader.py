"""
Test suite for JSON Reader module
"""

import unittest
import json
import os
import tempfile
from json_reader import (
    read_json_file,
    extract_specific_info,
    extract_nested_info,
    filter_list_by_criteria,
    get_all_values_by_key
)


class TestJsonReader(unittest.TestCase):
    """Test cases for JSON reader functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_data = {
            "users": [
                {
                    "id": 1,
                    "name": "John Doe",
                    "email": "john.doe@example.com",
                    "age": 30,
                    "city": "New York"
                },
                {
                    "id": 2,
                    "name": "Jane Smith",
                    "email": "jane.smith@example.com",
                    "age": 25,
                    "city": "San Francisco"
                }
            ],
            "metadata": {
                "version": "1.0",
                "created": "2025-10-18",
                "total_users": 2
            }
        }
        
        # Create a temporary JSON file for testing
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        json.dump(self.test_data, self.temp_file)
        self.temp_file.close()
    
    def tearDown(self):
        """Clean up test fixtures"""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_read_json_file_success(self):
        """Test reading a valid JSON file"""
        data = read_json_file(self.temp_file.name)
        self.assertEqual(data, self.test_data)
    
    def test_read_json_file_not_found(self):
        """Test reading a non-existent file"""
        with self.assertRaises(FileNotFoundError):
            read_json_file("nonexistent_file.json")
    
    def test_read_json_file_invalid_json(self):
        """Test reading a file with invalid JSON"""
        invalid_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        invalid_file.write("{ invalid json }")
        invalid_file.close()
        
        try:
            with self.assertRaises(json.JSONDecodeError):
                read_json_file(invalid_file.name)
        finally:
            os.unlink(invalid_file.name)
    
    def test_extract_specific_info_single_key(self):
        """Test extracting a single key from JSON data"""
        result = extract_specific_info(self.test_data, "metadata")
        self.assertEqual(result, self.test_data["metadata"])
    
    def test_extract_specific_info_multiple_keys(self):
        """Test extracting multiple keys from JSON data"""
        result = extract_specific_info(self.test_data, ["metadata", "users"])
        self.assertIn("metadata", result)
        self.assertIn("users", result)
        self.assertEqual(len(result), 2)
    
    def test_extract_specific_info_nonexistent_key(self):
        """Test extracting a non-existent key"""
        result = extract_specific_info(self.test_data, "nonexistent")
        self.assertIsNone(result)
    
    def test_extract_nested_info_simple_path(self):
        """Test extracting nested information with a simple path"""
        result = extract_nested_info(self.test_data, "metadata.version")
        self.assertEqual(result, "1.0")
    
    def test_extract_nested_info_array_index(self):
        """Test extracting from array using index"""
        result = extract_nested_info(self.test_data, "users.0.name")
        self.assertEqual(result, "John Doe")
    
    def test_extract_nested_info_deep_path(self):
        """Test extracting deeply nested information"""
        result = extract_nested_info(self.test_data, "users.1.email")
        self.assertEqual(result, "jane.smith@example.com")
    
    def test_extract_nested_info_invalid_path(self):
        """Test extracting with an invalid path"""
        result = extract_nested_info(self.test_data, "invalid.path.here")
        self.assertIsNone(result)
    
    def test_filter_list_by_criteria_single_criterion(self):
        """Test filtering a list by single criterion"""
        result = filter_list_by_criteria(
            self.test_data, 
            "users", 
            {"city": "New York"}
        )
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "John Doe")
    
    def test_filter_list_by_criteria_multiple_criteria(self):
        """Test filtering a list by multiple criteria"""
        result = filter_list_by_criteria(
            self.test_data,
            "users",
            {"city": "San Francisco", "age": 25}
        )
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "Jane Smith")
    
    def test_filter_list_by_criteria_no_match(self):
        """Test filtering with no matching criteria"""
        result = filter_list_by_criteria(
            self.test_data,
            "users",
            {"city": "Chicago"}
        )
        self.assertEqual(len(result), 0)
    
    def test_filter_list_by_criteria_invalid_list_key(self):
        """Test filtering with invalid list key"""
        result = filter_list_by_criteria(
            self.test_data,
            "nonexistent",
            {"city": "New York"}
        )
        self.assertEqual(result, [])
    
    def test_get_all_values_by_key(self):
        """Test getting all values for a specific key"""
        emails = get_all_values_by_key(self.test_data, "email")
        self.assertEqual(len(emails), 2)
        self.assertIn("john.doe@example.com", emails)
        self.assertIn("jane.smith@example.com", emails)
    
    def test_get_all_values_by_key_multiple_levels(self):
        """Test getting values from multiple nesting levels"""
        ids = get_all_values_by_key(self.test_data, "id")
        self.assertEqual(len(ids), 2)
        self.assertIn(1, ids)
        self.assertIn(2, ids)
    
    def test_get_all_values_by_key_not_found(self):
        """Test getting values for a non-existent key"""
        result = get_all_values_by_key(self.test_data, "nonexistent")
        self.assertEqual(result, [])


class TestJsonReaderWithSampleData(unittest.TestCase):
    """Test cases using the sample_data.json file"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.sample_file = "sample_data.json"
        # Only run these tests if sample_data.json exists
        if not os.path.exists(self.sample_file):
            self.skipTest("sample_data.json not found")
    
    def test_read_sample_file(self):
        """Test reading the sample data file"""
        data = read_json_file(self.sample_file)
        self.assertIn("users", data)
        self.assertIn("metadata", data)
    
    def test_extract_metadata_from_sample(self):
        """Test extracting metadata from sample file"""
        data = read_json_file(self.sample_file)
        metadata = extract_specific_info(data, "metadata")
        self.assertIsNotNone(metadata)
        self.assertIn("version", metadata)
    
    def test_filter_users_from_sample(self):
        """Test filtering users from sample file"""
        data = read_json_file(self.sample_file)
        sf_users = filter_list_by_criteria(data, "users", {"city": "San Francisco"})
        self.assertGreaterEqual(len(sf_users), 0)


if __name__ == "__main__":
    unittest.main()
