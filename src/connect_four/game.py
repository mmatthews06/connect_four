"""game.py - module for playing a game on the game board."""
from connect_four.game_board import GameBoard
from connect_four.game_board import GamePiece


class Game:
    """Game - manage the playing of a Connect Four game."""

    def __init__(self) -> None:
        """Initialize a new game."""
        self.game_board = GameBoard()
        self.player_one = GamePiece.RED
        self.player_two = GamePiece.YELLOW
        self.winner: GamePiece | None = None  # type: ignore

    def play(self) -> None:
        """Play a game that has been setup."""
        row_idx = 0
        active_player = self.player_one

        self.game_board.display()
        col_idx = int(input("Pick a column:"))
        self.game_board.play(active_player, col_idx)

        while not self.game_board.check_win(active_player, row_idx, col_idx):
            if active_player == GamePiece.RED:
                active_player = GamePiece.YELLOW
            else:
                active_player = GamePiece.RED

            print("-" * 40)
            self.game_board.display()
            col_idx = int(input("Pick a column:"))
            row_idx = self.game_board.play(active_player, col_idx)

        self.winner = active_player

        print("-" * 40)
        self.game_board.display()
        print(f"Congratulations, {self.winner}!")

    def player_won(self, piece: GamePiece) -> bool:
        """Return true if the specified piece is the game winner."""
        return self.winner == piece
