from enum import Enum
from typing import List
from typing import Tuple


class GamePiece(Enum):
    RED = 1
    YELLOW = 2


class GameBoard:
    NUM_ROWS: int = 6
    NUM_COLS: int = 7

    def __init__(self) -> None:
        self._diagonals = Diagonals()
        self._board: List[List[int]] = [
            [0 for j in range(self.NUM_COLS)] for i in range(self.NUM_ROWS)
        ]

    def board(self) -> List[List[int]]:
        return self._board

    def check_win(self, piece: GamePiece, rowIdx: int, colIdx: int) -> bool:
        """
        TODO: This is a fairly "low-level" method, something that doesn't
        require both rowIdx and colIdx could be done, but that likely means
        changing "play()", as well.
        """
        for sequence in self.neighborhood(rowIdx, colIdx):
            pieces_in_a_row = 0

            for board_piece in sequence:
                if board_piece == piece.value:
                    pieces_in_a_row += 1

                if pieces_in_a_row == 4:
                    return True

        return False

    def display(self) -> None:
        for row in self.board():
            print(" ".join([str(i) for i in row]))

    def neighborhood(self, rowIdx: int, colIdx: int) -> List[List[int]]:
        # TODO: Raise exception if either index is out of bounds.
        column_values = []
        first_diagonal = []
        second_diagonal = []

        # 1. get the column values.
        for row in self.board():
            column_values.append(row[colIdx])

        # 2. get the row values.
        row_values = self.board()[rowIdx]

        # 3. get diagonal that slopes upwards.
        for point in self._diagonals.get_up_diagonal(rowIdx, colIdx):
            piece = self.board()[point[0]][point[1]]
            first_diagonal.append(piece)

        # 4. get diagonal that slopes downwards.
        for point in self._diagonals.get_down_diagonal(rowIdx, colIdx):
            piece = self.board()[point[0]][point[1]]
            second_diagonal.append(piece)

        return [
            column_values,
            row_values,
            first_diagonal,
            second_diagonal,
        ]

    def play(self, piece: GamePiece, columnIdx: int) -> int:
        # TODO: Throw exception if column index out of range.
        # TODO: Throw exception if column is already full.
        last_empty_row = 0
        for rowIdx, row in enumerate(self.board()):
            if row[columnIdx] != 0:
                break

            last_empty_row = rowIdx

        self._board[last_empty_row][columnIdx] = piece.value

        return last_empty_row


class Diagonals:
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
        self.up_diagonals = {}
        self.down_diagonals = {}

        for diagonal in self.UPWARD_DIAGONALS:
            for point in diagonal:
                self.up_diagonals[point] = diagonal

        for diagonal in self.DOWNWARD_DIAGONALS:
            for point in diagonal:
                self.down_diagonals[point] = diagonal

    def get_up_diagonal(self, rowIdx: int, colIdx: int) -> List[Tuple[int, int]]:
        return self.up_diagonals.get((rowIdx, colIdx), [])

    def get_down_diagonal(self, rowIdx: int, colIdx: int) -> List[Tuple[int, int]]:
        return self.down_diagonals.get((rowIdx, colIdx), [])
