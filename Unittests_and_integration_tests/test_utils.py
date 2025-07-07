#!/usr/bin/env python3
"""add a comment for the module """
import unittest
from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import get_json
from utils import memoize
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the expected result."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        """Test that access_nested_map raises a KeyError for invalid path."""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)

        self.assertEqual(str(cm.exception), f"'{expected_key}'")


class TestGetJson(TestCase):
    """Tests for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    # patch actif pendant tout l'appel de la fonction
    @patch("utils.requests.get")
    # remplace requests.get par mock_get
    def test_get_json(self, test_url, test_payload, mock_get):
        """Tests for get_json function"""
        # recupère test_url et test_payload dans parameterized
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        # retourne test_playload
        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Tests for memoized function"""
    def test_memoize(self):
        """Test that memoize calls the method only once"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                """A memoized property"""
                return self.a_method()
        # patch spécifique à la méthode de la classe (local)
        with patch.object(
            TestClass, "a_method", return_value=42
        ) as mock_method:
            obj = TestClass()

            # premier appel, doit appeler a_method
            result1 = obj.a_property

            # deuxième appel, ne doit pas rappeler a_method
            result2 = obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


# python3 -m unittest -v test_utils.py pour un resultat test par test