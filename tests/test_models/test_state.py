#!/usr/bin/python3
"""Test State Representation"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """State Representation Test Suite"""

    def test_state_class_attributes(self):
        self.assertEqual(State.name, "")
