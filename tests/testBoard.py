#pylint: disable=C

import unittest
from unittest.mock import patch
from src.board import Board
from src.cell import Cell

class TestBoard(unittest.TestCase):
    
    def setUp(self) -> None:
        self.board = Board(5)

    def testBoardSize(self) -> None:
        self.assertEqual(self.board.getSize(), 5)

    def testGetCell(self) -> None:
        cell = self.board.getCell(2, 2)
        self.assertIsInstance(cell, Cell)

    def testPlaceTraps(self) -> None:
        self.board.placeTraps(0, 0)
        trapCount = sum(1 for x in range(5) for y in range(5) if self.board.getCell(x, y).isTrap())
        self.assertGreater(trapCount, 0)

    def testScanTraps(self) -> None:
        cell = self.board.getCell(1, 1)
        with patch.object(cell, "isTrap", return_value=True):
            with patch.object(cell, "scan") as mockScan:
                with patch.object(self.board, "displayBoard") as mockDisplay:
                    self.board.scanTraps()
                    mockScan.assert_called_once()
                    mockDisplay.assert_called_once()

    def testScanArea(self) -> None:
        self.board.getCell(2, 2).setAdjacentTraps(0)

        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = 2 + i, 2 + j
                if 0 <= nx < self.board.getSize() and 0 <= ny < self.board.getSize():
                    self.board.getCell(nx, ny).setAdjacentTraps(0)

        self.board.scanArea(2, 2)
        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = 2 + i, 2 + j
                if 0 <= nx < self.board.getSize() and 0 <= ny < self.board.getSize():
                    self.assertTrue(self.board.getCell(nx, ny).isScanned())


if __name__ == "__main__":
    unittest.main()
