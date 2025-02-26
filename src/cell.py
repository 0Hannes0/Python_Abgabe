class Cell:
    """eine Zelle im gameBoard"""
    
    def __init__(self, isTrap: bool = False):
        self._isTrap = isTrap
        self._adjacentTraps = 0
        self._isRevealed = False
        self._isScanned = False

    def isTrap(self) -> bool:
        """Gibt zurück, ob die Zelle eine Falle ist"""
        return self._isTrap
    
    def setAdjacentTraps(self, value) -> None:
        """Setzt die Anzahl der benachbarten Fallen"""
        self._adjacentTraps = value