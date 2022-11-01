#!/usr/bin/python3
"""Test City Representation"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """City Representation Test Suite"""

    def test_city_class_attributes(self):
        self.assertEqual(City.name, "")
        self.assertEqual(City.state_id, "")
