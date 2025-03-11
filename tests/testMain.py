"""
Testmodule für das Hauptprogramm main.py.
"""

import unittest
from unittest.mock import patch
import sys
import os
import src.main
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestMain(unittest.TestCase):
    """Testet die main-Funktionalität."""

    @patch("game.Game.start")
    def testMain(self, mockStart: unittest.mock.MagicMock) -> None:
        """Testet, ob main() Game.start() aufruft."""
        with patch("builtins.__name__", "__main__"):
            src.main.main()
        mockStart.assert_called_once()

if __name__ == "__main__":
    unittest.main()
