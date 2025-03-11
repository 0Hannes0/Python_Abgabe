"""
Testmodul für die Fehler
"""

import unittest
import sys
import os
from src.errors import OutOfRangeError
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestErrors(unittest.TestCase):
    """Testklasse für Fehler."""

    def testOutOfRangeError(self) -> None:
        """Testet die Fehlermeldung des OutOfRangeError."""
        error = OutOfRangeError(20, 5, 15)
        expectedMessage = "20 is out of the Possible Range (6-16)"
        self.assertEqual(str(error), expectedMessage)

if __name__ == "__main__":
    unittest.main()
