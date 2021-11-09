from unittest.mock import call
from unittest.mock import MagicMock
from unittest.mock import patch

from connect_four.game_board import Diagonals
from connect_four.game_board import GameBoard
from connect_four.game_board import GamePiece


def test_initial_board() -> None:
    gb = GameBoard()

    assert len(gb.board()) == 6


@patch("builtins.print")
def test_display(mock_print: MagicMock) -> None:
    """
    Testing the display method.
    """
    gb = GameBoard()
    gb.display()

    assert mock_print.mock_calls == [
        call("0 0 0 0 0 0 0"),
        call("0 0 0 0 0 0 0"),
        call("0 0 0 0 0 0 0"),
        call("0 0 0 0 0 0 0"),
        call("0 0 0 0 0 0 0"),
        call("0 0 0 0 0 0 0"),
    ]


def test_play_single() -> None:
    """
    Test a single "move" on the board.
    """
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


def test_play_full_column() -> None:
    """
    Try to fill the first column
    """
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


def test_play_full_last_column() -> None:
    """
    Try to fill the last column.
    """
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


def test_play_diagonal() -> None:
    """
    Play a game that leads to a stacked diagonal.
    """
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


def test_neighborhood_bottom_left() -> None:
    """
    The neighborhood method should return arrays with the
    correct dimensions.
    """
    gb = GameBoard()
    neighborhood = gb.neighborhood(5, 0)

    assert neighborhood == [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [],
    ]


def test_neighborhood_bottom_left_with_pieces() -> None:
    """
    The neighborhood method should return the correct values
    when the bottom row is partially full.
    """
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
        [],
    ]


def test_check_win_bottom_row() -> None:
    """
    Dropping pieces in 4 columns should cause a win.
    """
    gb = GameBoard()
    gb.play(GamePiece.RED, 0)
    gb.play(GamePiece.RED, 1)
    gb.play(GamePiece.RED, 2)
    rowIdx = gb.play(GamePiece.RED, 3)

    assert rowIdx == 5
    assert gb.check_win(GamePiece.RED, rowIdx, 3) == True


def test_check_win_column() -> None:
    """
    Dropping 4 pieces in the first column should deliver a win.
    """
    gb = GameBoard()
    gb.play(GamePiece.RED, 0)
    gb.play(GamePiece.RED, 0)
    gb.play(GamePiece.RED, 0)
    rowIdx = gb.play(GamePiece.RED, 0)

    assert rowIdx == 2
    assert gb.check_win(GamePiece.RED, rowIdx, 0) == True


def test_check_not_win_diff_column() -> None:
    """
    Filling the first column, but checking for a win in a different
    column should not cause a win.
    """
    gb = GameBoard()
    gb.play(GamePiece.RED, 0)
    gb.play(GamePiece.RED, 0)
    gb.play(GamePiece.RED, 0)
    rowIdx = gb.play(GamePiece.RED, 0)

    assert rowIdx == 2
    assert gb.check_win(GamePiece.RED, rowIdx, 2) == False


def test_check_win_diagonal() -> None:
    """
    Play a game that results in 4 RED values on the diagonal, should
    deliver a win.
    """
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


def test_check_not_win_with_gap() -> None:
    """
    A gap in the sequence on the bottom row should not indicate a win.
    """
    gb = GameBoard()
    gb.play(GamePiece.RED, 0)
    gb.play(GamePiece.RED, 1)
    gb.play(GamePiece.RED, 2)
    rowIdx = gb.play(GamePiece.RED, 4)

    assert rowIdx == 5
    assert gb.check_win(GamePiece.RED, rowIdx, 4) == False


def test_check_not_win_with_gap_in_diagonal() -> None:
    """
    A gap in the sequence on the diagonal should not indicate a win.
    """
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
    gb.play(GamePiece.YELLOW, 3)
    gb.play(GamePiece.YELLOW, 4)
    gb.play(GamePiece.YELLOW, 4)
    gb.play(GamePiece.YELLOW, 4)
    gb.play(GamePiece.YELLOW, 4)
    rowIdx = gb.play(GamePiece.RED, 4)

    assert rowIdx == 1
    assert gb.board() == [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 2, 2, 0, 0],
        [0, 0, 1, 2, 2, 0, 0],
        [0, 1, 2, 2, 2, 0, 0],
        [1, 2, 2, 2, 2, 0, 0],
    ]
    assert gb.check_win(GamePiece.RED, rowIdx, 4) == False


def test_diagonals_down() -> None:
    """
    The Diagonal helper class should return the right
    "downward", negatively sloped diagonal for a position.
    """
    diagonals = Diagonals()

    assert diagonals.get_down_diagonal(0, 4) == []
    assert diagonals.get_down_diagonal(0, 1) == [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6),
    ]


def test_diagonals_up() -> None:
    """
    The Diagonal helper class should return the right
    "upward", positively sloped diagonal for a position.
    """
    diagonals = Diagonals()

    assert diagonals.get_up_diagonal(0, 4) == [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
    assert diagonals.get_up_diagonal(0, 1) == []
