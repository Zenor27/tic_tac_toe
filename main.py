# Tic tac toe implementation
# AUTHORS: antoine.montes
# TODO: Rework on check_win

import sys
import os
import numpy as np
from io import StringIO

class Board:
    def __init__(self):
        self.array = []

        for i in range(3):
            self.array.append([])
            for j in range(3):
                self.array[i].append('-')

    def print(self):
        # Clear console
        os.system('cls' if os.name=='nt' else 'clear')
        print("row    => |0|1|2|")
        for i in range(3):
            print(f"line {i} => |", end='')
            for j in range(3):
                print(f"{self.array[i][j]}|", end='')
            print()


    def _check_rows(self, board):
        for row in board:
            if len(set(row)) == 1:
                return row[0]
        return 0

    def _check_diagonals(self):
        if len(set([self.array[i][i] for i in range(len(self.array))])) == 1:
            return self.array[0][0]
        if len(set([self.array[i][len(self.array) - i - 1] for i in range(len(self.array))])) == 1:
            return self.array[0][len(self.array) - 1]
        return 0

    def check_win(self):
        for board in [self.array, np.transpose(self.array)]:
            result = self._check_rows(board)
            if result:
                return result
        return self._check_diagonals()


class Player:
    def __init__(self, name, tick, board):
        self.name = name
        self.board = board
        self.tick = tick

    def _ask_line(self):
        line = input("Line: ")
        return int(line)


    def _ask_row(self):
        row = input("Row: ")
        return int(row)

    def play(self):
        print(f"Player {self.name} turn")
        line = self._ask_line()
        row = self._ask_row()

        board_position_value = self.board.array[line][row]

        if board_position_value != '-':
            print("Invalid position...")
            self.play()
        else:
            self.board.array[line][row] = self.tick


def get_player_name(i):
    return input(f"Player {i} name: ")


if __name__ == "__main__":
    board = Board()
    player_1_name = get_player_name(1)
    player_2_name = get_player_name(2)
    player_1 = Player(player_1_name, 'X', board)
    player_2 = Player(player_2_name, 'O', board)

    players = [player_1, player_2]

    while True:
        board.print()
        for player in players:
            player.play()

            print(board.check_win())
            if board.check_win() == player.tick:
                print(f"!!! Player {player.name} won !!!")
                exit(0)

            board.print()

