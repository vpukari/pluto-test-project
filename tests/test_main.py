"""
This is a example test fot the main.py
"""

import unittest
import app.main

class TestMain(unittest.TestCase):
    """
    This class is a example of a testcase
    """

    def test_main(self):
        result = app.main.example_function("Hello, world!")
        self.assertEqual(result, "Hello, world!")