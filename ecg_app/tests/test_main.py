"""Test module"""
import unittest
from unittest import TestCase


class TestMain(TestCase):
    """TestMain Class"""

    def test_main(self):
        """test_main.py docstring"""
        self.assertEqual(6, 3 * 2)


if __name__ == "__main__":
    unittest.main()
