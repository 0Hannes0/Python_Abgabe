#pylint: disable=C

import unittest
from src.cell import Cell

class TestCell(unittest.TestCase):

    def setUp(self) -> None:
        self.cell = Cell()
        self.trapCell = Cell(True)

    def testIsTrap(self) -> None:
        self.assertFalse(self.cell.isTrap())
        self.assertTrue(self.trapCell.isTrap())

    def testScan(self) -> None:
        self.assertFalse(self.cell.isScanned())
        self.cell.scan()
        self.assertTrue(self.cell.isScanned())

    def testAdjacentTraps(self) -> None:
        self.cell.setAdjacentTraps(3)
        self.assertEqual(self.cell.getAdjacentTraps(), 3)

if __name__ == "__main__":
    unittest.main()
