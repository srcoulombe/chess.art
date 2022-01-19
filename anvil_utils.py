# anvil_utils.py

# external dependencies
import matplotlib.pyplot as plt

import anvil.media
import anvil.server

# local dependencies
with open("anvil.key", "r") as handle:
    anvil_key = handle.readlines()[0]

anvil.server.connect(anvil_key)

# local dependencies
from pgn_parsing_utils import validate_pgn
from processing import get_moves, translate_moves, plot_translated_moves

@anvil.server.callable
def say_hello_from_uplink(name):
  print("Hello from the uplink, %s!" % name)
  return "Hello from the uplink, " + name

@anvil.server.callable
def generate_artwork_from_pgn(pgn: str, name: str):
    pgn_str = validate_pgn(pgn)
    print(pgn_str)
    moves = get_moves(pgn_str, fromfile=False)
    translated_moves = translate_moves(moves)
    fig = plot_translated_moves(translated_moves)
    plt.savefig(
        f"{name}.png"
    )
    return anvil.media.from_file(f"./{name}.png", f"image/{name}.png")

anvil.server.wait_forever()