#!/usr/bin/python3
"""Test User Model"""
import unittest

from models.user import User


class TestUser(unittest.TestCase):
    """Test Suite for User Model"""

    def test_class_attributes(self):
        """Test User class attributes"""
        self.assertEqual(type(User.email), type(""))
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

    def test_user_init(self):
        user_1 = User()
        self.assertEqual(user_1.email, "")
        self.assertEqual(user_1.password, "")
        self.assertEqual(user_1.first_name, "")
        self.assertEqual(user_1.last_name, "")
        user_1.email = "ammiel@yahoo.com"
        user_1.password = "password"
        user_1.first_name = "ammiel"
        user_1.last_name = "guy"
        self.assertEqual(user_1.email, "ammiel@yahoo.com")
        self.assertEqual(user_1.password, "password")
        self.assertEqual(user_1.first_name, "ammiel")
        self.assertEqual(user_1.last_name, "guy")
