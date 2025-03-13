"""
Tests für die Klasse Cell
"""

import unittest
from src.cell import Cell

class TestCell(unittest.TestCase):
    """Test für die Klasse Cell"""
    def setUp(self) -> None:
        """Setzt Standard-Zelle für Tests auf"""
        self.cell = Cell()
        self.trapCell = Cell(True)

    def testIsTrap(self) -> None:
        """Testet, ob Zelle korrekt als Falle erkannt wird"""
        self.assertFalse(self.cell.isTrap())
        self.assertTrue(self.trapCell.isTrap())

    def testScan(self) -> None:
        """Testet, ob Zelle aufgedeckt wird"""
        self.assertFalse(self.cell.isScanned())
        self.cell.scan()
        self.assertTrue(self.cell.isScanned())

    def testAdjacentTraps(self) -> None:
        """Testet Setzen und Abrufen angrenzender Fallen"""
        self.cell.setAdjacentTraps(3)
        self.assertEqual(self.cell.getAdjacentTraps(), 3)

if __name__ == "__main__":
    unittest.main()
