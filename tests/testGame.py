#pylint: disable=C

import unittest
from unittest.mock import patch, MagicMock
from src.game import Game, GameState

class TestGame(unittest.TestCase):

    def setUp(self) -> None:
        self.game = Game()
        self.game._size = 5  # pylint: disable=protected-access
        self.game._moves = 0  # pylint: disable=protected-access
        self.game._gameBoard = MagicMock()  # pylint: disable=protected-access

        self.mockBoard = self.game._gameBoard  # pylint: disable=protected-access

        self.minePositions = {(1, 1), (2, 3), (3, 2), (4, 4)}

        def getCellMock(x: int, y: int) -> MagicMock:
            cell = MagicMock()
            cell.isScanned.return_value = False
            cell.isTrap.return_value = (x, y) in self.minePositions
            return cell

        self.mockBoard.getCell.side_effect = getCellMock

    def testGameStart(self) -> None:
        with patch.object(self.game, "_initializeGameBoard") as mockInit, \
             patch.object(self.game, "_getGameBoard") as mockGetBoard, \
             patch.object(self.game, "_gameLoop") as mockGameLoop:

            mockBoardInstance = MagicMock()
            mockGetBoard.return_value = mockBoardInstance

            self.game.start()

            mockInit.assert_called_once()
            mockGetBoard.assert_called_once()
            mockBoardInstance.displayBoard.assert_called_once()
            mockGameLoop.assert_called_once()

    def testInitializeGameBoardValid(self) -> None:
        with patch("builtins.input", return_value="7"):
            self.game._initializeGameBoard()  # pylint: disable=protected-access
            self.assertEqual(self.game._size, 7)  # pylint: disable=protected-access
            self.assertIsNotNone(self.game._gameBoard)  # pylint: disable=protected-access

    def testInitializeGameBoardInvalid(self) -> None:
        with patch("builtins.input", side_effect=["2", "16", "8"]):
            self.game._initializeGameBoard()  # pylint: disable=protected-access
            self.assertEqual(self.game._size, 8)  # pylint: disable=protected-access

    def testHandleMoveHitTrap(self) -> None:
        x, y = 2, 2
        result = self.game._handleMove(x, y)  # pylint: disable=protected-access
        self.assertEqual(result, GameState.LOST, f"Erwartet: {GameState.LOST}, Erhalten: {result}")

    def testHandleMoveSafeCell(self) -> None:
        result: GameState = self.game._handleMove(1, 1)  # pylint: disable=protected-access
        self.assertEqual(result, GameState.PLAYING)

    def testCheckWinFalse(self) -> None:
        self.mockBoard.getCell.return_value.isTrap.return_value = False
        self.mockBoard.getCell.return_value.isScanned.return_value = False
        result: GameState = self.game._checkWin()  # pylint: disable=protected-access
        self.assertEqual(result, GameState.PLAYING)

    def testCheckWinTrue(self) -> None:
        def getCellMock(x: int, y: int) -> MagicMock:
            cell: MagicMock = MagicMock()
            cell.isTrap.return_value = (x, y) in self.minePositions
            cell.isScanned.return_value = not cell.isTrap()
            return cell

        self.mockBoard.getCell.side_effect = getCellMock
        result: GameState = self.game._checkWin()  # pylint: disable=protected-access
        self.assertEqual(result, GameState.WON)

    def testEndGameExit(self) -> None:
        with patch("builtins.input", side_effect=["n"]), self.assertRaises(SystemExit):
            self.game._end()  # pylint: disable=protected-access

    def testLoseCondition(self) -> None:
        with patch.object(self.game, "_handleMove", return_value=GameState.LOST), \
             patch.object(self.game, "_getGameBoard") as mockBoard, \
             patch.object(self.game, "_end") as mockEnd, \
             patch("builtins.input", side_effect=["1", "1"]):

            self.game._gameLoop()  # pylint: disable=protected-access
            mockBoard.return_value.scanTraps.assert_called_once()
            mockEnd.assert_called_once()

if __name__ == "__main__":
    unittest.main()
