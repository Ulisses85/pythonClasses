import unittest
from average import AverageCalculator

def analyze_text():
    pass


class TestCalc(unittest.TestCase):
    """Tests for the minimal() function"""

    def test_function_runs(self):
        """Basic smoke test: does the function run"""
        mode = average.AverageCalculator.mode
        mode(self)


if __name__ == "__main__":
    unittest.main()
