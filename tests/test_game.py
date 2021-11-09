
from unittest.mock import patch

from connect_four.game import Game
from connect_four.game_board import GamePiece

def test_game_play():
    """
    A simple game where both players try to fill up columns 1 and 2, should cause player 1, the RED player, to win.
    """
    moves = [0, 1, 0, 1, 0, 1, 0]
    def mock_input(s):
        return moves.pop(0)

    game = Game()
    with patch('connect_four.game.input', mock_input):
        game.play()

    assert game.player_won(GamePiece.RED)
