from tictactoe.cell_occupied_exception import CellOccupiedException
from tictactoe.tac_constant import Tacconstant


class Tictactoe:

    def __init__(self):
        self.table = []
        for i in range(3):
            self.row = []
            for j in range(3):
                self.row.append(Tacconstant.EMPTY)
            self.table.append(self.row)

    def checkTable(self, number):
        table = number - 1
        row = table // 3
        column = table % 3
        return self.table[row][column]

    def player1_plays(self, user_input):
        self.validate_play(user_input)
        table = user_input - 1
        row = table // 3
        column = table % 3
        self.table[row][column] = Tacconstant.X

    def player2_plays(self, user_input):
        self.validate_play(user_input)
        table = user_input - 1
        row = table // 3
        column = table % 3
        self.table[row][column] = Tacconstant.O

    @staticmethod
    def validate_play(number):
        table = number - 1
        row = table // 3
        column = table % 3

        if number[row][column] == Tacconstant.EMPTY:
            table[row][column] = Tacconstant.X
            table[row][column] = Tacconstant.O
        raise CellOccupiedException("cell has been played")
