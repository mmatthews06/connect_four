
from typing import List, Tuple
from unittest.mock import call, patch, MagicMock

from connect_four.game_board import Diagonals, GameBoard
from connect_four.game_board import GamePiece

def play(gameBoard: GameBoard, plays: List[Tuple[int, GamePiece]]):
    for colIdx, piece in plays:
        gameBoard.play(piece, colIdx)


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


def test_play_diagonal():
    gb = GameBoard()
    gb.play(GamePiece.RED, 0)
    gb.play(GamePiece.YELLOW, 1)
    gb.play(GamePiece.RED, 1)
    gb.play(GamePiece.YELLOW, 2)
    gb.play(GamePiece.YELLOW, 2)
    gb.play(GamePiece.RED, 2)
    gb.play(GamePiece.YELLOW, 3)
    gb.play(GamePiece.YELLOW, 3)
    gb.play(GamePiece.YELLOW, 3)
    gb.play(GamePiece.RED, 3)

    assert gb.board() == [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 2, 0, 0, 0],
        [0, 1, 2, 2, 0, 0, 0],
        [1, 2, 2, 2, 0, 0, 0],
    ]


def test_neighborhood_bottom_left():
    gb = GameBoard()
    neighborhood = gb.neighborhood(5, 0)

    assert neighborhood == [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        []
    ]


def test_neighborhood_bottom_left_with_pieces():
    gb = GameBoard()
    gb.play(GamePiece.RED, 0)
    gb.play(GamePiece.RED, 1)
    gb.play(GamePiece.RED, 2)
    gb.play(GamePiece.RED, 3)

    neighborhood = gb.neighborhood(5, 0)

    assert neighborhood == [
        [0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        []
    ]


def test_check_win_bottom_row():
    gb = GameBoard()
    gb.play(GamePiece.RED, 0)
    gb.play(GamePiece.RED, 1)
    gb.play(GamePiece.RED, 2)
    rowIdx = gb.play(GamePiece.RED, 3)

    assert rowIdx == 5
    assert gb.check_win(GamePiece.RED, rowIdx, 3) == True


def test_check_win_column():
    gb = GameBoard()
    gb.play(GamePiece.RED, 0)
    gb.play(GamePiece.RED, 0)
    gb.play(GamePiece.RED, 0)
    rowIdx = gb.play(GamePiece.RED, 0)

    assert rowIdx == 2
    assert gb.check_win(GamePiece.RED, rowIdx, 0) == True


def test_check_not_win_diff_column():
    gb = GameBoard()
    gb.play(GamePiece.RED, 0)
    gb.play(GamePiece.RED, 0)
    gb.play(GamePiece.RED, 0)
    rowIdx = gb.play(GamePiece.RED, 0)

    assert rowIdx == 2
    assert gb.check_win(GamePiece.RED, rowIdx, 2) == False


def test_check_win_diagonal():
    gb = GameBoard()
    gb.play(GamePiece.RED, 0)
    gb.play(GamePiece.YELLOW, 1)
    gb.play(GamePiece.RED, 1)
    gb.play(GamePiece.YELLOW, 2)
    gb.play(GamePiece.YELLOW, 2)
    gb.play(GamePiece.RED, 2)
    gb.play(GamePiece.YELLOW, 3)
    gb.play(GamePiece.YELLOW, 3)
    gb.play(GamePiece.YELLOW, 3)
    rowIdx = gb.play(GamePiece.RED, 3)

    assert rowIdx == 2
    assert gb.check_win(GamePiece.RED, rowIdx, 3) == True


def test_diagonals_down():
    diagonals = Diagonals()

    assert diagonals.get_down_diagonal(0, 4) == []
    assert diagonals.get_down_diagonal(0, 1) == [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]


def test_diagonals_up():
    diagonals = Diagonals()

    assert diagonals.get_up_diagonal(0, 4) == [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
    assert diagonals.get_up_diagonal(0, 1) == []