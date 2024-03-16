from unittest import TestCase

from tictactoe import tictactoe_game
from tictactoe.tac_constant import Tacconstant
from tictactoe.tictactoe_game import Tictactoe


class Tictactoetest(TestCase):

    def test_that_every_index_of_board_is_empty(self):
        self.assertEqual(Tacconstant.EMPTY, Tacconstant.EMPTY)

    def test_that_the_value_of_the_cell_can_change_if_player_plays(self):
        tictactoe = Tictactoe()
        tictactoe.player1_plays(3)
        self.assertEqual(Tacconstant.X,tictactoe.checkTable(3))

    def test_player_cannot_play_in_an_occupied_cell(self):
        tictactoe = Tictactoe()
        tictactoe.player1_plays(4)
        self.assertEqual(Tacconstant.X,tictactoe.checkTable(4))
        tictactoe.player2_plays(4)
        self.assertEqual(Tacconstant.O,tictactoe.checkTable(4))


