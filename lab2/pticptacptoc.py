# # pTic-pTac-pToc
# ## Instalation
# 1. Install Python (recommended min. 3.8)
# 2. Install EasyAI:
# pip3 install easyAI
# or
# pip install easyAI
# ## Run
# python3 pticptacptoc.py
# or
# python pticptacptoc.py
# ## Rules of the game
# ENG:
# [Tic-Tac-Toe](https://en.wikipedia.org/wiki/Tic-tac-toe)
# PL:
# [Kółko i krzyżyk](https://pl.wikipedia.org/wiki/K%C3%B3%C5%82ko_i_krzy%C5%BCyk)
# You start 😃

# ## About & Creators
# -   Jakub Pilachowski s17999
# -   Michał Ptok s16665

from easyAI import AI_Player, Negamax
from easyAI import TwoPlayersGame
from easyAI.Player import Human_Player


class PticPtacPtoc(TwoPlayersGame):
    """
    TicTacToe console game with AI opponent based on TwoPlayersGame from EasyAI Python library
    
    """

    def __init__(self, players):
        """
        The constructor for TicTacToe class.

        Parameters:
        players (array): The Human_Player and AI_Player
        """
        self.players = players
        self.winningCombo = 3
        self.size = 3
        self.init_board()
        self.nplayer = 1

    def init_board(self):
        """
        The function to initialize board with zeros.
        """
        board = []
        for _ in range(self.size):
            board.append([0 for j in range(self.size)])
        self.board = board

    def is_opponent(self, x, y):
        """
        The function to something opponent.

        Parameters:
            x (int): the 'x' axis coordinate
            y (int): the 'y' axis coordinate

        Returns:
            (bool) true is field is taken by opponent
        """
        return self.board[x][y] == self.nopponent

    def check_row(self, row):
        """
        The function to check row combo.

        Parameters:
            row (int): row number

        Returns:
            (bool): true if combo is in this row
        """
        for column in range(self.winningCombo):
            if not self.is_opponent(row, column):
                return False
        return True

    def check_rows(self):
        """
        The function to check rows combo.

        Returns:
            (bool): true if combo is in the rows
        """
        for row in range(self.winningCombo):
            if self.check_row(row):
                return True
        return False

    def check_column(self, column):
        """
        The function to check column combo.

        Parameters:
            column (int): column number

        Returns:
            (bool): true if combo is in this column
        """
        for row in range(self.winningCombo):
            if not self.is_opponent(row, column):
                return False
        return True

    def check_columns(self):
        """
        The function to check columns combo.

        Returns:
            (bool): true if combo is in the columns
        """
        for column in range(self.winningCombo):
            if self.check_column(column):
                return True
        return False

    def check_right_diagonal(self):
        """
        The function to check diagonal (from top left to right) combo.

        Returns:
            (bool): true if combo is in this diagonal
        """
        for i in range(self.winningCombo):
            if not self.is_opponent(i, i):
                return False
        return True

    def check_left_diagonal(self):
        """
        The function to check diagonal (from top right to left) combo.

        Returns:
            (bool): true if combo is in this diagonal
        """
        for i in range(self.winningCombo):
            if not self.is_opponent(i, self.winningCombo-1-i):
                return False
        return True

    def possible_moves(self):
        """
        The function to return possible moves.

        Returns:
            possible_moves (array): list of moves that player can take
        """
        possible_moves = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    possible_moves.append(str(i + 1) + " " + str(j + 1))
        return possible_moves

    def make_move(self, move):
        """
        The function to make move move.

        Parameters:
            move (string): coordiantes of next move that player is taking
        """
        x, y = map(int, move.split())
        x -= 1
        y -= 1
        self.board[x][y] = self.nplayer

    def unmake_move(self, move):
        """
        The function to undo the move.

        Parameters:
            move (string): coordiantes of the move that player wants to undo
        """
        x, y = map(int, move.split())
        x -= 1
        y -= 1
        self.board[x][y] = 0

    def lose(self):
        """
        The function to check every possibility of losing

        Returns:
            (bool): true if lose
        """
        return self.check_columns() or self.check_rows() or self.check_right_diagonal() or self.check_left_diagonal()

    def is_over(self):
        """
        The function to check if there are any moves left

        Returns:
            (bool): true if no moves left
        """
        return (self.possible_moves() == []) or self.lose()

    def show(self):
        """
        The function to display the board.
        """
        print('\\', end=' ')
        for x in range(self.size):
            print(x+1, end=' ')
        print('')
        for i in range(self.size):
            print(i+1, end=' ')
            for j in range(self.size):
                if self.board[i][j] == 1:
                    print("0", end=' ')
                elif self.board[i][j] == 2:
                    print("X", end=' ')
                else:
                    print(".", end=' ')
            print("")

    def scoring(self):
        """
        The function to score player

        Returns:
        score (int): -1000 when lose, 500 when win
        """
        return -1000 if self.lose() else 500


if __name__ == "__main__":
    from easyAI import AI_Player, Negamax
    ai_algo = Negamax(6)
    PticPtacPtoc([Human_Player(), AI_Player(ai_algo)]).play()

