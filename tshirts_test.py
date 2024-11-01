import unittest

from tshirts import size

class TestSizeClassification(unittest.TestCase):
    def test_size_small(self):
        """Test that measurements below 38 are classified as 'S'."""
        self.assertEqual(size(37), 'S')
    
    def test_size_small_boundary(self):
        """Test boundary value where size transitions to 'M'."""
        self.assertEqual(size(38), 'S')

    def test_size_medium(self):
        """Test that measurements between 39 and 41 are classified as 'M'."""
        self.assertEqual(size(39), 'M')

    def test_size_large(self):
        """Test that measurements of 42 and above are classified as 'L'."""
        self.assertEqual(size(42), 'L')
        self.assertEqual(size(43), 'L')

    def test_negative_size(self):
        """Test that negative values raise an exception."""
        with self.assertRaises(ValueError) as context:
            size(-1)
        self.assertEqual(str(context.exception), "Negative size is not possible")

if __name__ == '__main__':
    unittest.main()
