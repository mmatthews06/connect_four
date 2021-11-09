"""Test cases for the __main__ module."""
from unittest.mock import patch

import pytest
from click.testing import CliRunner

from connect_four import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    moves = [0, 1, 0, 1, 0, 1, 0]

    def mock_input(s: str) -> int:
        return moves.pop(0)

    with patch("connect_four.game.input", mock_input):
        result = runner.invoke(__main__.main)

    assert result.exit_code == 0
