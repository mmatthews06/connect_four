"""A connect four game board class, and supporting types."""
from enum import Enum
from typing import List
from typing import Tuple


class GamePiece(Enum):
    """Represents a game piece, which can be either RED or YELLOW."""

    RED = 1
    YELLOW = 2


class GameBoard:
    """A connect four game board, with methods to put pieces in, check for a win, etc.

    The board is a 2x2 array, with 6 rows and 7 columns. Future implementations may use a Board
    strategy implemented in numpy, or something else.
    """

    NUM_ROWS: int = 6
    NUM_COLS: int = 7

    def __init__(self) -> None:
        """Initialize the game board. Right now, it does not take any inputs."""
        self._diagonals = Diagonals()
        self._board: List[List[int]] = [
            [0 for j in range(self.NUM_COLS)] for i in range(self.NUM_ROWS)
        ]

    def board(self) -> List[List[int]]:
        """Get a representation of the board."""
        return self._board

    def check_win(self, piece: GamePiece, row_idx: int, col_idx: int) -> bool:
        """Check whether there is a win on the board for the given pieces, given the row and column indexes.

        TODO: This is a fairly "low-level" method, something that doesn't
        require both row_idx and col_idx could be done, but that likely means
        changing "play()", as well.
        """
        for sequence in self.neighborhood(row_idx, col_idx):
            pieces_in_a_row = 0

            for board_piece in sequence:
                if board_piece == piece.value:
                    pieces_in_a_row += 1
                else:
                    pieces_in_a_row = 0

                if pieces_in_a_row == 4:
                    return True

        return False

    def display(self) -> None:
        """Print the curent board to the console."""
        for row in self.board():
            print(" ".join([str(i) for i in row]))

    def neighborhood(self, row_idx: int, col_idx: int) -> List[List[int]]:
        """Get the "neighborhood" of a given row/column index.

        That is, return the pieces on the row, column and both diagonals for the given index.
        """
        # TODO: Raise exception if either index is out of bounds.
        column_values = []
        first_diagonal = []
        second_diagonal = []

        # 1. get the column values.
        for row in self.board():
            column_values.append(row[col_idx])

        # 2. get the row values.
        row_values = self.board()[row_idx]

        # 3. get diagonal that slopes upwards.
        for point in self._diagonals.get_up_diagonal(row_idx, col_idx):
            piece = self.board()[point[0]][point[1]]
            first_diagonal.append(piece)

        # 4. get diagonal that slopes downwards.
        for point in self._diagonals.get_down_diagonal(row_idx, col_idx):
            piece = self.board()[point[0]][point[1]]
            second_diagonal.append(piece)

        return [
            column_values,
            row_values,
            first_diagonal,
            second_diagonal,
        ]

    def play(self, piece: GamePiece, column_idx: int) -> int:
        """Place the given piece in the column (at the top of the board), and update the board with the piece.

        This method returns the row where the piece ended up. That is, the piece falls to the row that is returned.
        """
        # TODO: Throw exception if column index out of range.
        # TODO: Throw exception if column is already full.
        last_empty_row = 0
        for row_idx, row in enumerate(self.board()):
            if row[column_idx] != 0:
                break

            last_empty_row = row_idx

        self._board[last_empty_row][column_idx] = piece.value

        return last_empty_row


class Diagonals:
    """A class that pre-computes positive/upward-sloped and negative/downward-sloped diagonals for indexes."""

    UPWARD_DIAGONALS: List[List[Tuple[int, int]]] = [
        [(0, 3), (1, 2), (2, 1), (3, 0)],
        [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)],
        [(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)],
        [(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1)],
        [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2)],
        [(2, 6), (3, 5), (4, 4), (5, 3)],
    ]

    DOWNWARD_DIAGONALS: List[List[Tuple[int, int]]] = [
        [(0, 3), (1, 4), (2, 5), (3, 6)],
        [(0, 2), (1, 3), (2, 4), (3, 5), (4, 6)],
        [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)],
        [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
        [(1, 0), (2, 1), (3, 2), (4, 3), (5, 4)],
        [(2, 0), (3, 1), (4, 2), (5, 3)],
    ]

    def __init__(self) -> None:
        """Initialize the diagonals given the indexes above."""
        self.up_diagonals = {}
        self.down_diagonals = {}

        for diagonal in self.UPWARD_DIAGONALS:
            for point in diagonal:
                self.up_diagonals[point] = diagonal

        for diagonal in self.DOWNWARD_DIAGONALS:
            for point in diagonal:
                self.down_diagonals[point] = diagonal

    def get_up_diagonal(self, row_idx: int, col_idx: int) -> List[Tuple[int, int]]:
        """Return the positive/upward-sloped diagonal for the given row/column index pair."""
        return self.up_diagonals.get((row_idx, col_idx), [])

    def get_down_diagonal(self, row_idx: int, col_idx: int) -> List[Tuple[int, int]]:
        """Return the negative/downward-sloped diagonal for the given row/column index pair."""
        return self.down_diagonals.get((row_idx, col_idx), [])
