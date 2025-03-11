import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):
    @patch("game.Game.start")
    def testMain(self, mockStart: unittest.mock.MagicMock) -> None:
        """Testet, ob main() Game.start() aufruft."""
        with patch("builtins.__name__", "__main__"):
            main.main()
        mockStart.assert_called_once()

if __name__ == "__main__":
    unittest.main()

