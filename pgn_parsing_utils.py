# pgn_parsing_utils.py

# standard library dependencies
import os
from io import StringIO

# external dependencies
import chess.pgn

def format_pgn_str(game_pgn_string: str) -> str:
    return game_pgn_string.replace("\n", " ")

def read_pgn_file(fp: str) -> str:
    with open(fp, 'r') as handle:
        contents = "".join(handle.readlines())
    return format_pgn_str(contents)

def read_pgn(game_pgn_string: str) -> str:
    return format_pgn_str(game_pgn_string)

def validate_pgn_file(fp: str) -> str:
    assert os.path.isfile(fp)
    game_pgn_string = read_pgn_file(fp)
    try:
        _ = chess.pgn.read_game(
            StringIO(game_pgn_string)
        )
    except Exception as error:
        raise Exception(f"Failed to parse the game from '{fp}': '{game_pgn_string}'") from error
    else:
        return game_pgn_string

def validate_pgn(game_pgn_string: str) -> str:
    game_pgn_string = read_pgn(game_pgn_string)
    try:
        _ = chess.pgn.read_game(
            StringIO(game_pgn_string)
        )
    except Exception as error:
        raise Exception(f"Failed to parse the game: '{game_pgn_string}'") from error
    else:
        return game_pgn_string