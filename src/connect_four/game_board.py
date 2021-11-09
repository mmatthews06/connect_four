
from enum import Enum
from typing import List


class GamePiece(Enum):
    RED = 1
    YELLOW = 2


class GameBoard():
    NUM_ROWS = 6
    NUM_COLS = 7

    def __init__(self) -> None:
        self._board: List[List[int]] = [
            [0 for j in range(self.NUM_COLS)]
            for i in range(self.NUM_ROWS)
        ]

    def board(self) -> List[List[int]]:
        return self._board

    def display(self) -> None:
        for row in self.board():
            print(' '.join([str(i) for i in row]))


    def play(self, piece: GamePiece, columnIdx: int):
        # TODO: Throw exception if column index out of range.
        # TODO: Throw exception when column is full.
        last_empty_row = 0
        for rowIdx, row in enumerate(self.board()):
            if row[columnIdx] != 0:
                break

            last_empty_row = rowIdx

        self._board[last_empty_row][columnIdx] = piece.value
