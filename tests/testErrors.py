"""
Tests für die Klasse Fehler
"""

import unittest
from src.errors import OutOfRangeError

class TestErrors(unittest.TestCase):
    """Tests für die Klasse Fehler"""

    def testOutOfRangeError(self) -> None:
        """Testet Fehlermeldung des OutOfRangeError"""
        error = OutOfRangeError(20, 5, 15)
        expectedMessage = "20 is out of the Possible Range (6-16)"
        self.assertEqual(str(error), expectedMessage)

if __name__ == "__main__":
    unittest.main()
