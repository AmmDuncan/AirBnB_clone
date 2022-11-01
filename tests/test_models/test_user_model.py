#!/usr/bin/python3
"""Test User Model"""
import unittest

from models.user import User


class TestUserModel(unittest.TestCase):
    """Test Suite for User Model"""

    def test_class_attributes(self):
        self.assertEqual(type(User.email), type(""))
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
