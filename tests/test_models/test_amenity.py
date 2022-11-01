#!/usr/bin/python3
"""Test Amenity Representation"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Amenity Representation Test Suite"""

    def test_amenity_class_attributes(self):
        self.assertEqual(Amenity.name, "")
