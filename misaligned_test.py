from misaligned import *
import unittest
from io import StringIO
import sys

class TestPrintColorMap(unittest.TestCase):

    def setUp(self):
        """Redirect stdout to capture print output for each test."""
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        """Reset stdout after each test."""
        sys.stdout = sys.__stdout__

    def test_output_line_count(self):
        """Verify that print_color_map produces exactly 25 lines of output."""
        print_color_map()
        sys.stdout = sys.__stdout__
        output_lines = self.captured_output.getvalue().strip().split('\n')
        self.assertEqual(len(output_lines), 25, "Expected 25 lines of color mapping output")

    def test_format_alignment(self):
        """Check that each line has exactly three parts separated by '|' and all values are properly aligned."""
        print_color_map()
        sys.stdout = sys.__stdout__
        output_lines = self.captured_output.getvalue().strip().split('\n')

        for index, line in enumerate(output_lines):
            parts = line.split('|')
            # Ensure each line has three parts: index, major color, and minor color
            self.assertEqual(len(parts), 3, f"Line {index} should have exactly three parts separated by '|': {line}")
            
            # Ensure the first part is an integer index and matches the expected order
            try:
                line_index = int(parts[0].strip())
                self.assertEqual(line_index, index, f"Expected index {index} but found {line_index} in line {line}")
            except ValueError:
                self.fail(f"Line index is not an integer at line {index}: {line}")

    def test_major_color_alignment(self):
        """Ensure that the major color names are left-aligned and have at least four characters for readability."""
        print_color_map()
        sys.stdout = sys.__stdout__
        output_lines = self.captured_output.getvalue().strip().split('\n')

        for index, line in enumerate(output_lines):
            parts = line.split('|')
            major_color = parts[1].strip()
            self.assertGreaterEqual(len(major_color), 4, f"Major color name '{major_color}' is misaligned at line {index}: {line}")

    def test_minor_color_alignment(self):
        """Ensure that the minor color names are left-aligned and have at least four characters for readability."""
        print_color_map()
        sys.stdout = sys.__stdout__
        output_lines = self.captured_output.getvalue().strip().split('\n')

        for index, line in enumerate(output_lines):
            parts = line.split('|')
            minor_color = parts[2].strip()
            self.assertGreaterEqual(len(minor_color), 4, f"Minor color name '{minor_color}' is misaligned at line {index}: {line}")

    def test_integer_index(self):
        """Check that the first part of each line is an integer index."""
        print_color_map()
        sys.stdout = sys.__stdout__
        output_lines = self.captured_output.getvalue().strip().split('\n')

        for index, line in enumerate(output_lines):
            parts = line.split('|')
            try:
                int(parts[0].strip())
            except ValueError:
                self.fail(f"Expected integer index but found non-integer value at line {index}: {line}")

if __name__ == '__main__':
    unittest.main()
