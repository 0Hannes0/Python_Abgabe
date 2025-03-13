#pylint: disable=C

import unittest
from src.errors import OutOfRangeError

class TestErrors(unittest.TestCase):

    def testOutOfRangeError(self) -> None:
        error = OutOfRangeError(20, 5, 15)
        expectedMessage = "20 is out of the Possible Range (6-16)"
        self.assertEqual(str(error), expectedMessage)

if __name__ == "__main__":
    unittest.main()
