import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from unittest.mock import patch, MagicMock
from game import Game, GameState
import errors

class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        """Setzt ein Spiel mit einem Mock-Spielfeld auf"""
        self.game = Game()
        self.game._size = 5  
        self.game._moves = 0
        self.game._gameBoard = MagicMock()

        self.mock_board = self.game._gameBoard

        self.mine_positions = {(1, 1), (2, 3), (3, 2), (4, 4)}

        def get_cell_mock(x: int, y: int) -> MagicMock:
            cell = MagicMock()
            cell.isScanned.return_value = False
            cell.isTrap.return_value = (x, y) in self.mine_positions  # Hier überprüfen!
            return cell

        self.mock_board.getCell.side_effect = get_cell_mock

    def test_game_start(self) -> None:
        """Testet, ob das Spiel korrekt gestartet wird"""
        with patch.object(self.game, "_initializeGameBoard") as mock_init, \
            patch.object(self.game, "_getGameBoard") as mock_get_board, \
            patch.object(self.game, "_gameLoop") as mock_game_loop:
            
            mock_board_instance = MagicMock()
            mock_get_board.return_value = mock_board_instance

            self.game.start()

            mock_init.assert_called_once()
            mock_get_board.assert_called_once()
            mock_board_instance.displayBoard.assert_called_once()
            mock_game_loop.assert_called_once()

    def test_initialize_game_board_valid_size(self) -> None:
        """Testet, ob ein gültiges Spielfeld initialisiert wird"""
        with patch("builtins.input", return_value="7"):
            self.game._initializeGameBoard()
            self.assertEqual(self.game._size, 7)
            self.assertIsNotNone(self.game._gameBoard)

    def test_initialize_game_board_invalid_size(self) -> None:
        """Testet falsche Eingabe für die Spielfeldgröße"""
        with patch("builtins.input", side_effect=["2", "16", "8"]):  # Zuerst falsche Eingaben, dann gültig
            self.game._initializeGameBoard()
            self.assertEqual(self.game._size, 8)

    def test_handle_move_hit_trap(self) -> None:
        """Testet, ob das Spiel endet, wenn eine Mine getroffen wird"""
        x, y = 2, 2
        result = self.game._handleMove(x, y)
        self.assertEqual(result, GameState.LOST, f"Erwartet: {GameState.LOST}, Erhalten: {result}")

    def test_handle_move_safe_cell(self) -> None:
        """Testet, ob das Spiel weitergeht, wenn ein sicheres Feld gewählt wird"""
        result: GameState = self.game._handleMove(1, 1)
        self.assertEqual(result, GameState.PLAYING)

    def test_check_win_false(self) -> None:
        """Testet, ob das Spiel weiterspielt, wenn nicht alle Felder aufgedeckt wurden"""
        self.mock_board.getCell.return_value.isTrap.return_value = False
        self.mock_board.getCell.return_value.isScanned.return_value = False
        result: GameState = self.game._checkWin()
        self.assertEqual(result, GameState.PLAYING)

    def test_check_win_true(self) -> None:
        """Testet, ob das Spiel gewonnen wird, wenn alle sicheren Felder aufgedeckt sind"""
        def get_cell_mock(x: int, y: int) -> MagicMock:
            cell: MagicMock = MagicMock()
            cell.isTrap.return_value = (x, y) in self.mine_positions
            cell.isScanned.return_value = not cell.isTrap()
            return cell

        self.mock_board.getCell.side_effect = get_cell_mock
        result: GameState = self.game._checkWin()
        self.assertEqual(result, GameState.WON)

    def test_end_game_play_again(self) -> None:
        """Testet, ob das Spiel neu startet, wenn der Spieler 'y' eingibt"""
        with patch("builtins.input", side_effect=["y"]), patch("game.Game.start") as mock_start:
            self.game._end()
            mock_start.assert_called_once()

    def test_end_game_exit(self) -> None:
        """Testet, ob das Spiel sich beendet, wenn der Spieler 'n' eingibt"""
        with patch("builtins.input", side_effect=["n"]), self.assertRaises(SystemExit):
            self.game._end()

    def test_game_loop_lose_condition(self) -> None:
        """Testet, ob das Spiel korrekt endet, wenn eine Mine getroffen wird"""
        with patch.object(self.game, "_handleMove", return_value=GameState.LOST), \
            patch.object(self.game, "_getGameBoard") as mock_board, \
            patch.object(self.game, "_end") as mock_end, \
            patch("builtins.input", side_effect=["1", "1"]):  # Mine bei (1,1)

            self.game._gameLoop()

            # Prüft, ob scanTraps() aufgerufen wurde, weil der Spieler verloren hat
            mock_board.return_value.scanTraps.assert_called_once()
            
            # Prüft, ob das Spiel danach endet
            mock_end.assert_called_once()



if __name__ == "__main__":
    unittest.main()
