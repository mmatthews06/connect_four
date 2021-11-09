
from unittest.mock import patch

from connect_four.game import Game
from connect_four.game_board import GamePiece

def test_game_play():
    moves = [0, 1, 0, 1, 0, 1, 0]
    def mock_input():
        return moves.pop(0)

    game = Game()
    with patch('connect_four.input', mock_input):
        game.play()

    assert game.player_won(GamePiece.RED)