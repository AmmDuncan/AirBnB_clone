#!/usr/bin/python3
from datetime import datetime
from time import sleep
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class behavior"""

    def test_init(self):
        """Test initialization behavior"""
        base_1 = BaseModel()
        base_2 = BaseModel()
        self.assertIsInstance(base_1, BaseModel)
        self.assertNotEqual(base_1.id, base_2.id)
        self.assertEqual(base_1.created_at.date(), datetime.now().date())

    def test_str(self):
        """Test string representation method of BaseModel instances"""
        base_3 = BaseModel()
        self.assertRegex(str(base_3), r"^\[.+\]\s\(.+\)\s.+$")

    def test_save(self):
        """Test save method on BaseModel instances"""
        base_4 = BaseModel()
        updated_at_on_init = base_4.updated_at
        sleep(0.5)
        base_4.save()
        self.assertNotEqual(updated_at_on_init, base_4.updated_at)

    def test_to_dict(self):
        """Test to_dict method on BaseModel instances"""
        base_5 = BaseModel()
        base_5_dict = base_5.to_dict()
        self.assertEqual(base_5_dict["__class__"], "BaseModel")

    def test_init_with_dict(self):
        """Test initialization with dictionary"""
        base_6 = BaseModel()
        base_6_dict = base_6.to_dict()
        base_7 = BaseModel(**base_6_dict)
        self.assertEqual(base_6.id, base_7.id)
        self.assertEqual(base_6.created_at, base_7.created_at)
