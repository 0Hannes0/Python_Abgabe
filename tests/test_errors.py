import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from errors import OutOfRangeError

class TestErrors(unittest.TestCase):
    def testOutOfRangeErrorMessage(self) -> None:
        """Testet die Fehlermeldung des OutOfRangeError."""
        error = OutOfRangeError(20, 5, 15)
        expected_message = "20 is out of the Possible Range (6-16)"
        self.assertEqual(str(error), expected_message)
    
if __name__ == "__main__":
    unittest.main()