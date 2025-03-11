"""Startet das Spiel"""

from src.game import Game

def main() -> None:
    """Startet das Spiel"""
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
