import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from gameBoard import Board
from cell import Cell
from unittest.mock import MagicMock, patch


class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        """Setzt ein Standard-Spielfeld für Tests auf."""
        self.board = Board(5)
    
    def testBoardSize(self) -> None:
        """Testet, ob die Größe korrekt gespeichert wird."""
        self.assertEqual(self.board.getSize(), 5)
    
    def testGetCell(self) -> None:
        """Testet, ob eine Zelle korrekt abgerufen wird."""
        cell = self.board.getCell(2, 2)
        self.assertIsInstance(cell, Cell)
    
    def testPlaceTraps(self) -> None:
        """Testet, ob Fallen gesetzt werden."""
        self.board.placeTraps(0, 0)
        trapCount = sum(1 for x in range(5) for y in range(5) if self.board.getCell(x, y).isTrap())
        self.assertGreater(trapCount, 0)
    
    def testScanTraps(self) -> None:
        """Testet, ob scanTraps() alle Fallen aufdeckt und displayBoard() aufruft."""

        cell = self.board._grid[1][1]
        with patch.object(cell, "isTrap", return_value=True):
            with patch.object(cell, "scan") as mock_scan:
                with patch.object(self.board, "displayBoard") as mock_display:
                    self.board.scanTraps()
                    mock_scan.assert_called_once()
                    mock_display.assert_called_once()

    def testScanArea(self) -> None:
        """Testet, ob scanArea rekursiv leere Felder aufdeckt."""
        self.board._grid[2][2] = Cell(False)  
        self.board._grid[2][2].setAdjacentTraps(0)

        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = 2 + i, 2 + j
                if 0 <= nx < self.board.getSize() and 0 <= ny < self.board.getSize():
                    self.board._grid[nx][ny] = Cell(False)  
                    self.board._grid[nx][ny].setAdjacentTraps(0)

        self.board.scanArea(2, 2)
        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = 2 + i, 2 + j
                if 0 <= nx < self.board.getSize() and 0 <= ny < self.board.getSize():
                    self.assertTrue(self.board.getCell(nx, ny).isScanned())


    
if __name__ == "__main__":
    unittest.main()
