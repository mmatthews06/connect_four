"""Command-line interface."""
import click

from connect_four.game import Game


@click.command()
@click.version_option()
def main() -> None:
    """Connect_Four."""
    game = Game()
    game.play()


if __name__ == "__main__":
    main(prog_name="connect_four")  # pragma: no cover
