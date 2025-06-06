import importlib.util
import pathlib

# Load the tictactoe module from the python directory without executing its CLI
spec = importlib.util.spec_from_file_location(
    "tictactoe",
    pathlib.Path(__file__).resolve().parents[1] / "tictactoe.py",
)
tictactoe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tictactoe)


def reset_board():
    tictactoe.board = [
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9",
    ]


def test_checkwin_horizontal():
    reset_board()
    tictactoe.board[0:3] = ["X", "X", "X"]
    assert tictactoe.checkwin("X")


def test_checkwin_vertical():
    reset_board()
    tictactoe.board[0] = tictactoe.board[3] = tictactoe.board[6] = "X"
    assert tictactoe.checkwin("X")


def test_checkwin_diagonal():
    reset_board()
    tictactoe.board[0] = tictactoe.board[4] = tictactoe.board[8] = "X"
    assert tictactoe.checkwin("X")


def test_checkdraw_full_board_no_win():
    tictactoe.board = [
        "X", "O", "X",
        "X", "O", "O",
        "O", "X", "X",
    ]
    assert tictactoe.checkdraw()
    assert not tictactoe.checkwin("X")
    assert not tictactoe.checkwin("O")

