"""Spielfeld von Verlassene Raumstation"""

import random
from cell import Cell

class Board:
    """Spielfeld von Verlassene Raumstation"""

    def __init__(self, size: int) -> None:
        self._size: int = size
        self._grid: list[list[Cell]] = [[Cell() for _ in range(size)] for _ in range(size)]

    def getCell(self, x: int, y: int) -> Cell:
        """Gibt die Zelle an den Koordinaten zurück"""
        return self._grid[x][y]

    def getSize(self) -> int:
        """Gibt die Größe des Spielfelds zurück"""
        return self._size

    def placeTraps(self, dx: int, dy: int) -> None:
        """Platziert Fallen zufällig auf dem Spielfeld"""
        for x in range(self._size):
            for y in range(self._size):
                self._grid[x][y] = Cell(random.choices([True, False], [0.3, 0.7])[0])
        self._grid[dx][dy] = Cell()
        self._calculateAdjacentTraps()

    def _calculateAdjacentTraps(self) -> None:
        """Berechnet Anzahl der benachbarten Fallen"""
        for x in range(self._size):
            for y in range(self._size):
                if not self._grid[x][y].isTrap():
                    trapCount = self._countTraps(x, y)
                    self._grid[x][y].setAdjacentTraps(trapCount)

    def _countTraps(self, x, y) -> int:
        """Zählt die Fallen um die Zelle"""
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = x + i, y + j
                if not(0 <= nx < self._size and 0 <= ny < self._size):
                    continue
                if self._grid[nx][ny].isTrap():
                    count += 1
        return count

    def revealArea(self, x: int, y: int) -> None:
        """Aufdecken leerer Felder"""
        if not (0 <= x < self._size and 0 <= y < self._size):
            return
        if self._grid[x][y].isRevealed():
            return

        self._grid[x][y].reveal()

        if self._grid[x][y].getAdjacentTraps() == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    nx, ny = x + i, y + j
                    if 0 <= nx < self._size and 0 <= ny < self._size:
                        self.revealArea(nx, ny)

    def displayBoard(self) -> None:
        """Zeigt das Spielfeld"""
        for row in self._grid:
            for cell in row:
                if cell.isRevealed():
                    if cell.isTrap():
                        print("*", end=" ")
                    else:
                        count = cell.getAdjacentTraps()
                        print(count if count > 0 else " ", end=" ")
                else:
                    print("■", end=" ")
            print()

    def revealTraps(self) -> None:
        """Deckt alle Fallen auf"""
        for row in self._grid:
            for cell in row:
                if cell.isTrap():
                    cell.reveal()
        self.displayBoard()
