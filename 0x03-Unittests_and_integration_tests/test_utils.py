#!/usr/bin/env python3
"""
Unittest for utils.access_nested_map
"""
from parameterized import parameterized
from utils import access_nested_map
import unittest



class TestAccessNestedMap (unittest.TestCase):
    """
    TestAccessNestedMap class for 
    testing access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, res):
        """
        Testcases for nested map function
        """
        self.assertEqual(access_nested_map(nested_map, path), res)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("b",), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, res):
        """
        Testcases for error handling
        """
        self.assertRaises(res, access_nested_map, nested_map, path)


if __name__ == "__main__":
    unittest.main()
