
# standard library dependencies
from typing import List, Tuple

# external dependencies
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import patheffects

# local dependencies
from diy_chess import ChessGame

def get_moves(pgn_fp: str, fromfile: bool = True):
    game = ChessGame(pgn_fp, fromfile=fromfile)
    moves = []
    while not game.is_finished:
        moves.append(game.next())
    return moves

def translate_moves(moves_list: List[Tuple[str, str]]) -> List[Tuple[int, int]]:
    map_ = {letter:integer 
        for integer, letter in 
        enumerate(('a','b','c','d','e','f','g','h'), start=1)
    }
    translated_moves = []
    for move in moves_list:
        print(move)
        if move is not None: 
            source, dest = move
            if source is None or dest is None: 
                continue
            source_ = map_[source[0]], int(source[1])
            dest_ = map_[dest[0]], int(dest[1])
            translated_moves.append((source_, dest_))
    return translated_moves

def plot_translated_moves(  translated_moves: List[Tuple[str, str]],
                            filepath: str = None):
    color = "white"
    colors = []
    for i in range(len(translated_moves)):
        colors.append(color)
        if color == "white":
            color = "black"
        else:
            color = "white"
    fig, ax = plt.subplots()
    ax.set_facecolor('gray')
    for i, (source, dest) in enumerate(translated_moves):
        color = "white" if i%2 == 0 else "black"
        plt.plot(
            [source[0], dest[0]], 
            [source[1], dest[1]],
            color=color,
            linewidth=4,
            #solid_capstyle='round',
            path_effects=[
                patheffects.SimpleLineShadow(shadow_color="red", linewidth=5),
                patheffects.Normal()
            ]
        )
    ax.autoscale()
    ax.set_ylim(0,9)
    ax.set_xlim(0,9)
    ax.margins(0.1)
    for spine in ax.spines.values():
        spine.set_visible(False)
    plt.tick_params(
        axis='both',       
        which='both',      
        bottom=False,      
        left=False,        
        labelleft=False,
        labelbottom=False  
    ) 
    return fig
