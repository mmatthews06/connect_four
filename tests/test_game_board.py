

from unittest.mock import call
from unittest.mock import patch
from unittest.mock import MagicMock

from connect_four.game_board import GameBoard
from connect_four.game_board import GamePiece

def test_initial_board() -> None:
    gb = GameBoard()

    assert len(gb.board()) == 6


@patch('builtins.print')
def test_display(mock_print: MagicMock) -> None:
    gb = GameBoard()
    gb.display()

    assert mock_print.mock_calls == [
        call('0 0 0 0 0 0 0'),
        call('0 0 0 0 0 0 0'),
        call('0 0 0 0 0 0 0'),
        call('0 0 0 0 0 0 0'),
        call('0 0 0 0 0 0 0'),
        call('0 0 0 0 0 0 0'),
    ]


def test_play_single():
    gb = GameBoard()

    gb.play(GamePiece.RED, 0)

    assert gb.board() == [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
    ]

def test_play_full_column():
    gb = GameBoard()

    for _ in range(GameBoard.NUM_ROWS):
        gb.play(GamePiece.RED, 0)

    assert gb.board() == [
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
    ]

def test_play_full_last_column():
    gb = GameBoard()

    for _ in range(GameBoard.NUM_ROWS):
        gb.play(GamePiece.YELLOW, 6)

    assert gb.board() == [
        [0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 2],
    ]