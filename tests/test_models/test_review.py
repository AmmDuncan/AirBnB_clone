#!/usr/bin/python3
"""Test Review Representation"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Review Representation Test Suite"""

    def test_review_class_attributes(self):
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
