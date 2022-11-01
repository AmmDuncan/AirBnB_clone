#!/usr/bin/python3
"""Test File Storage Engine"""
import os
import unittest

from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test suite for FileStorage engine"""

    def test_save(self):
        """Test save method"""
        filename = 'file.json'
        FileStorage._FileStorage__file_path = filename
        storage_inst = FileStorage()
        storage_inst.save()

        with open(filename, 'r') as file:
            self.asset(file.read(), "{}")

        os.remove(filename)
