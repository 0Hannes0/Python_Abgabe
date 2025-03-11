import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from cell import Cell

class TestCell(unittest.TestCase):
    def setUp(self) -> None:
        """Setzt eine Standard-Zelle für Tests auf."""
        self.cell = Cell()
        self.trapCell = Cell(True)
    
    def testIsTrap(self) -> None:
        """Testet, ob eine Zelle korrekt als Falle erkannt wird."""
        self.assertFalse(self.cell.isTrap())
        self.assertTrue(self.trapCell.isTrap())
    
    def testScan(self) -> None:
        """Testet, ob eine Zelle aufgedeckt wird."""
        self.assertFalse(self.cell.isScanned())
        self.cell.scan()
        self.assertTrue(self.cell.isScanned())
    
    def testAdjacentTraps(self) -> None:
        """Testet das Setzen und Abrufen angrenzender Fallen."""
        self.cell.setAdjacentTraps(3)
        self.assertEqual(self.cell.getAdjacentTraps(), 3)
    
if __name__ == "__main__":
    unittest.main()
