import random
from cell import Cell

class Board:
    """Spielfeld von Verlassene Raumstation"""
    
    def __init__(self, size: int) -> None:
        self._size: int = size
        self._grid: list[list[Cell]] = [[Cell() for _ in range(size)] for _ in range(size)]
        self._minesPlaced: bool = False

    def placeMines(self) -> None:
        """Platziert Minen zufällig auf dem Spielfeld"""
        for x in range(self._size):
            for y in range(self._size):
                x, y = random.randint(0, self._size - 1), random.randint(0, self._size - 1)
                self._grid[x][y] = Cell(True)

        self._calculateAdjacentTraps()
        self._minesPlaced = True

    def _calculateAdjacentTraps(self) -> None:
        """Berechnet Anzahl der benachbarten Minen"""
        for x in range(self._size):
            for y in range(self._size):
                if not self._grid[x][y].isTrap():
                    trapCount = self.countTraps(x, y)
                    self._grid[x][y].setAdjacentTraps(trapCount)

    def countTraps(self, x, y) -> int:
        """Zählt die Fallen um die Zelle"""
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self._grid[x+i][y+j].isTrap():
                    count += 1
        return count