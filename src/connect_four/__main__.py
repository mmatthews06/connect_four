"""Command-line interface."""
import click

from .game_board import GameBoard


@click.command()
@click.version_option()
def main() -> None:
    """Connect_Four."""
    gb = GameBoard()
    gb.display()

    return 0


if __name__ == "__main__":
    main(prog_name="connect_four")  # pragma: no cover
