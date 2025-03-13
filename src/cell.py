"""Eine Zelle im gameBoard"""

class Cell:
    """Eine Zelle im gameBoard"""

    def __init__(self, isTrap: bool = False):
        self._isTrap: bool = isTrap
        self._adjacentTraps: int = 0
        self._isScanned: bool = False

    def getAdjacentTraps(self) -> int:
        """Gibt die Anzahl benachbarter Fallen zurück"""
        return self._adjacentTraps

    def isScanned(self) -> bool:
        """Gibt zurück, ob Zelle aufgedeckt wurde"""
        return self._isScanned

    def isTrap(self) -> bool:
        """Gibt zurück, ob Zelle eine Falle ist"""
        return self._isTrap

    def setAdjacentTraps(self, value: int) -> None:
        """Setzt Anzahl benachbarter Fallen"""
        self._adjacentTraps = value

    def scan(self) -> None:
        """Deckt Zelle auf"""
        self._isScanned = True
