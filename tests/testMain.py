#pylint: disable=C

import unittest
from unittest.mock import patch
import src.main

class TestMain(unittest.TestCase):

    @patch("src.game.Game.start")
    def testMain(self, mockStart: unittest.mock.MagicMock) -> None:
        with patch("builtins.__name__", "__main__"):
            src.main.main()
        mockStart.assert_called_once()

if __name__ == "__main__":
    unittest.main()
