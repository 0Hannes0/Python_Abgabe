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
        possiblePositions = []
        totalCells = self._size ** 2
        numTraps = round(totalCells * 0.156)
        for x in range(self._size):
            for y in range(self._size):
                if(x, y) != (dx, dy):
                    possiblePositions.append((x, y))
        trapPositions = random.sample(possiblePositions, numTraps)
        for x, y in trapPositions:
            self._grid[x][y] = Cell(True)
        self._calculateAdjacentTraps()

    def _calculateAdjacentTraps(self) -> None:
        """Berechnet Anzahl der benachbarten Fallen"""
        for x in range(self._size):
            for y in range(self._size):
                if not self._grid[x][y].isTrap():
                    trapCount = self._countTraps(x, y)
                    self._grid[x][y].setAdjacentTraps(trapCount)

    def _countTraps(self, x: int, y: int) -> int:
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

    def scanArea(self, x: int, y: int) -> None:
        """Aufdecken leerer Felder"""
        if not (0 <= x < self._size and 0 <= y < self._size):
            return
        if self._grid[x][y].isScanned():
            return

        self._grid[x][y].scan()

        if self._grid[x][y].getAdjacentTraps() == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    nx, ny = x + i, y + j
                    if 0 <= nx < self._size and 0 <= ny < self._size:
                        self.scanArea(nx, ny)

    def displayBoard(self) -> None:
        """Zeigt das Spielfeld"""
        print("   ", end="")
        for y in range(self._size):
            print(f"{y+1:2}", end=" ")
        print("\n  " + "—" * (self._size * 3))

        for row in range(self._size):
            print(f"{row+1:2}|", end=" ")

            for cell in self._grid[row]:
                if cell.isScanned():
                    if cell.isTrap():
                        print("*", end="  ")
                    else:
                        count = cell.getAdjacentTraps()
                        print(count if count > 0 else " ", end="  ")
                else:
                    print("■", end="  ")
            print()

    def scanTraps(self) -> None:
        """Deckt alle Fallen auf"""
        for row in self._grid:
            for cell in row:
                if cell.isTrap():
                    cell.scan()
        self.displayBoard()
