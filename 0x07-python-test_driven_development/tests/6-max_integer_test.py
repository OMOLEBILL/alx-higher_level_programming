#!/usr/bin/python3
"""unit tests
"""


from unittest import TestCase
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_not_int(self):
        """Test with a list of non-ints and ints:
        should raise a TypeError exception"""
        ln = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, ln)

    def test_regular(self):
        """Test with a regular list of ints: should return the max result"""
        ln = [1, 2, 3, 4, 5]
        result = max_integer(ln)
        self.assertEqual(result, 5)

    def test_empty(self):
        """Test with an empty list: should return None"""
        ln = []
        result = max_integer(ln)
        self.assertEqual(result, None)

    def test_negative(self):
        """Test with a list of negative values: should return the max"""
        ln = [-2, -6, -1]
        result = max_integer(ln)
        self.assertEqual(result, -1)

    def test_float(self):
        """Test with a list of mixed ints and floats: should return the max"""
        ln = [3, 4.5, 2]
        result = max_integer(ln)
        self.assertEqual(result, 4.5)

    def test_no_args(self):
        """Check: no arguments passed to func"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Check: only one number"""
        test_ele = [10]
        self.assertEqual(max_integer(test_ele), 10)


if __name__ == "__main__":
    unittest.main()
