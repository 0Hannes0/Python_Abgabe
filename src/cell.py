"""ine Zelle im gameBoard"""

class Cell:
    """Eine Zelle im gameBoard"""

    def __init__(self, isTrap: bool = False):
        self._isTrap: bool = isTrap
        self._adjacentTraps: int = 0
        self._isRevealed: bool = False

    def getAdjacentTraps(self) -> int:
        """Gibt die Anzahl der benachbarten Fallen zurück"""
        return self._adjacentTraps

    def isRevealed(self) -> bool:
        """Gibt zurück, ob die Zelle aufgedeckt wurde"""
        return self._isRevealed

    def isTrap(self) -> bool:
        """Gibt zurück, ob die Zelle eine Falle ist"""
        return self._isTrap

    def setAdjacentTraps(self, value) -> None:
        """Setzt die Anzahl der benachbarten Fallen"""
        self._adjacentTraps = value

    def reveal(self) -> None:
        """Deckt die Zelle auf"""
        self._isRevealed = True
