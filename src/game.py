"""Verwarltet Spiellogik"""

from enum import Enum
import sys
from gameBoard import Board
import errors

# pylint: disable=too-few-public-methods
class GameState(Enum):
    """Spielzustände"""
    WON = "won"
    LOST = "lost"
    PLAYING = "playing"
    REPEAT = "repeat"

class Game:
    """Verwaltet Spiellogik"""
    minSize = 5
    maxSize = 15

    def __init__(self) -> None:
        self._gameBoard: Board | None = None
        self._size: int = 0
        self._moves: int = 0

    def _getGameBoard(self) -> Board:
        """Stellt sicher dass gameBoard nicht None ist"""
        assert self._gameBoard is not None, "GameBoard is not initialized"
        return self._gameBoard


    def start(self) -> None:
        """Startet Spiel und verwaltet Benutzereingaben"""
        print("-----------------Welcome-----------------")
        self._initializeGameBoard()
        self._getGameBoard().displayBoard()
        self._gameLoop()

    def _end(self) -> None:
        print("-----------------------------------------")
        while True:
            again = input("Do you want to play again? (y/n): ").strip().lower()
            if again == "y":
                self._gameBoard = None
                self._moves = 0
                self.start()
                return
            if again == "n":
                print("Goodbye!")
                print("-----------------------------------------")
                sys.exit()
            print("Invalid Input!")


    def _initializeGameBoard(self) -> None:
        """Fragt Spielfeldgröße ab und erstellt Spielfeld"""
        while True:
            try:
                self._size = int(input("Please enter the size of the game table: "))
                if self._size < self.minSize or self._size > self.maxSize:
                    raise errors.OutOfRangeError(self._size, self.minSize-1, self.maxSize-1)
                break
            except ValueError:
                print("Please enter a valid number.")
            except errors.OutOfRangeError as e:
                print(e)

        self._gameBoard = Board(self._size)

    def _gameLoop(self) -> None:
        """Hauptspiel-Schleife"""
        while True:
            try:
                x = int(input("Please enter line of the row: "))
                if not 1 <= x <= self._size:
                    raise errors.OutOfRangeError(x, 0, self._size - 1)
                y = int(input("Please enter line of the column: "))
                if not 1 <= y <= self._size:
                    raise errors.OutOfRangeError(y, 0, self._size - 1)

                if self._moves == 0:
                    self._getGameBoard().placeTraps(x-1, y-1)

                state = self._handleMove(x, y)
                if state == GameState.WON:
                    print("Congratulations! You won the game!")
                    break

                if state == GameState.LOST:
                    self._getGameBoard().scanTraps()
                    print("Game Over! You hit a trap.")
                    break

                if state == GameState.REPEAT:
                    print("This cell is already scanned.")

            except ValueError:
                print("Please enter a valid number.")
            except errors.OutOfRangeError as e:
                print(e)
        self._end()

    def _handleMove(self, x: int, y: int) -> GameState:
        """Verarbeitet den Spielzug"""
        cell = self._getGameBoard().getCell(x-1, y-1)
        if cell.isScanned():
            return GameState.REPEAT
        self._moves += 1
        if cell.isTrap():
            return GameState.LOST
        self._getGameBoard().scanArea(x-1, y-1)
        self._getGameBoard().displayBoard()
        return self._checkWin()

    def _checkWin(self) -> GameState:
        """Prüft, ob alle nicht-Fallen-Felder aufgedeckt wurden"""
        for x in range(self._size):
            for y in range(self._size):
                cell = self._getGameBoard().getCell(x, y)
                if not cell.isTrap() and not cell.isScanned():
                    return GameState.PLAYING
        return GameState.WON


if __name__ == "__main__":
    game = Game()
    game.start()
