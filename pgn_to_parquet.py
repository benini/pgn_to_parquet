import os
import sys
import chess.pgn
import pandas as pd

def read_pgn(pgn_path):
    games = []
    with open(pgn_path) as pgn:
        while True:
            game = chess.pgn.read_game(pgn)
            if game is None:
                break
            game_info = dict(game.headers)
            game_info['Date'] = pd.to_datetime(game_info['Date'])
            exporter = chess.pgn.StringExporter(headers=False, variations=True, comments=True)
            game_info["__movetext__"] = game.accept(exporter)
            games.append(game_info)
    return games

def export_to_parquet(games, parquet_path):
    df = pd.DataFrame(games)
    df.to_parquet(parquet_path, compression="ZSTD")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        pgn_file_path = sys.argv[1]
    else:
        print("Usage: python pgn_to_parquet.py path_to_pgn_file [path_to_parquet_file]")
        sys.exit(1)

    if len(sys.argv) > 2:
        parquet_file_path = sys.argv[2]
    else:
        parquet_file_path = os.path.splitext(pgn_file_path)[0] + '.parquet'

    games = read_pgn(pgn_file_path)
    export_to_parquet(games, parquet_file_path)
