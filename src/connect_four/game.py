
from connect_four.game_board import GameBoard, GamePiece

class Game():
    def __init__(self) -> None:
        self.game_board = GameBoard()

    def play(self) -> None:
        pass

    def player_won(self, piece: GamePiece) -> bool:
        return False