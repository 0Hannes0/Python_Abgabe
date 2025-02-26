import random
from cell import Cell

class Board:
    """Spielfeld von Minesweeper"""
    
    def __init__(self, size: int) -> None:
        self._size: int = size
        self._grid: list[list[Cell]] = [[Cell() for _ in range(size)] for _ in range(size)]
        self._minesPlaced: bool = False

    def placeMines(self):
        """Platziert Minen zufällig auf dem Spielfeld, außer auf dem ersten Klick."""
        minePositions = set()
        for x, y in self._grid:
            x, y = random.randint(0, self._size - 1), random.randint(0, self._size - 1)
            minePositions.add((x, y))

        for x, y in minePositions:
            self._grid[x][y] = Cell(True)

        self._minesPlaced = True
