from unittest.mock import patch

from connect_four.game import Game
from connect_four.game_board import GamePiece


def test_game_play_simple() -> None:
    """
    A simple game where both players try to fill up columns 1 and 2, should cause player 1, the RED player, to win.
    """
    moves = [0, 1, 0, 1, 0, 1, 0]

    def mock_input(s) -> int:
        return moves.pop(0)

    game = Game()
    with patch("connect_four.game.input", mock_input):
        game.play()

    assert game.player_won(GamePiece.RED)


def test_game_play_simple_yellow() -> None:
    """
    A simple game where YELLOW blocks, then continues to fill its column, should cause YELLOW to win.
    """
    moves = [0, 1, 0, 1, 0, 0, 0, 1, 0, 1]

    def mock_input(s) -> int:
        return moves.pop(0)

    game = Game()
    with patch("connect_four.game.input", mock_input):
        game.play()

    assert game.player_won(GamePiece.YELLOW)


def test_game_play_diagonal() -> None:
    """
    RED should be able to fill the diagonal while YELLOW does nothing but help.
    """
    moves = [0, 1, 1, 2, 2, 3, 2, 3, 3, 5, 3]

    def mock_input(s) -> int:
        return moves.pop(0)

    game = Game()
    with patch("connect_four.game.input", mock_input):
        game.play()

    assert game.player_won(GamePiece.RED)


def test_game_play_yellow_bottom_row() -> None:
    """
    RED tries to fill the diagonal, but YELLOW should snag the bottom row.
    """
    moves = [0, 1, 1, 2, 2, 3, 2, 3, 3, 4]

    def mock_input(s) -> int:
        return moves.pop(0)

    game = Game()
    with patch("connect_four.game.input", mock_input):
        game.play()

    assert game.player_won(GamePiece.YELLOW)
