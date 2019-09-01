import csv
import os
from scripts.ChessGame import ChessGame


def convert_pgn_to_csv(filename):
    current_game = ChessGame()
    previous_line_metadata = True

    f = open(f'../data/pgn/{filename}')
    line = f.readline()
    csv_file = open(f"../data/csv/{filename.split('.')[0]}.csv", 'w', newline='')
    wr = csv.writer(csv_file, delimiter=',')

    while line:
        if line.__contains__("["):
            # Line contains metadata

            name = line[1:].split(" ", 1)[0]
            value = line[1:].split('"', 1)[1].split('"')[0]

            if line.__contains__("Event"):
                # New game
                current_game = ChessGame(value)
                current_game.moves = []
            else:
                current_game.__setattr__(name.lower(), value)
                previous_line_metadata = True

        elif line.__eq__("\n"):
            # Line is empty
            if not previous_line_metadata:
                wr.writerow(list(current_game.__iter__()))
                previous_line_metadata = True

        else:
            # Line contains gamedata
            moves_on_line = line.split(".")
            moves_on_line.pop(0)
            for move in moves_on_line:
                move = move.rsplit(" ")
                current_game.moves.append([move[0], move[1]])
            previous_line_metadata = False

        line = f.readline()
    f.close()


class PGNReader:
    for filename in os.listdir("../data/pgn/"):
        if filename.endswith(".pgn") and filename != "SultanKhan.pgn" and filename != "TorreRepetto.pgn":
            # SultanKhan and TorreRepetto have a different format, known issue and not worth fixing
            print(filename)
            convert_pgn_to_csv(filename)
            continue
        else:
            continue
