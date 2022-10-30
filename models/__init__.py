#!/usr/bin/python3
"""Instantiate and keep storage updated with engine"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
