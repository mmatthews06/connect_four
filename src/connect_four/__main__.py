"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Connect_Four."""


if __name__ == "__main__":
    main(prog_name="connect_four")  # pragma: no cover
