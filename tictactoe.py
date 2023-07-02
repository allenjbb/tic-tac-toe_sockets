# ##################################################################################### #
# Allen Blanton
# CS 372 Fall 2022
# Project 4: Client-Server Chat
#
# A simple implementation of TicTacToe.
# ##################################################################################### #

class TicTacToe:

    def __init__(self):
        self._board = Board()
        self._player = 'X'  # used to alternate between X's turn and O's turn
        self._state = 'CONTINUE'  # used to keep track of game state

    # Returns the board a string
    def get_board(self):
        return self._board.get_board()

    # Attempts to make the given move, returning True if successful or False otherwise
    def make_move(self, move):
        if self._board.make_move(move, self._player):
            self.update_state()
            return True
        return False

    # Updates the game state
    def update_state(self):
        if not self._board.get_moves():
            self._state = 'DRAW'
        elif self._board.is_winner():
            self._state = f'{self._player} WINS'
        self._player = 'O' if self._player == 'X' else 'X'

    def get_state(self):
        return self._state

    def get_player(self):
        return self._player


class Board:

    def __init__(self):
        self._board = [[1, 2, 3],  # game board data
                       [4, 5, 6],
                       [7, 8, 9]]
        self._moves = {  # remaining legal moves
            '1': (0, 0),
            '2': (0, 1),
            '3': (0, 2),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '7': (2, 0),
            '8': (2, 1),
            '9': (2, 2)
        }

    # Attempts to make the given move for the given player, returning True if successful
    # or False otherwise
    def make_move(self, move, player):
        if move in self._moves.keys():
            r, c = self._moves[move]
            self._board[r][c] = player  # make the move
            self._moves.pop(move)  # remove the move from the pool of possible moves
            return True  # move was successful
        return False  # move was unsuccessful

    def get_moves(self):
        return self._moves

    # Checks the rows for a win
    def check_horizontals(self):
        for row in self._board:
            if row[0] == row[1] == row[2]:
                return True
        return False

    # Checks the columns for a win
    def check_verticals(self):
        for col in range(3):
            if self._board[0][col] == self._board[1][col] == self._board[2][col]:
                return True
        return False

    # Checks the diagonals for a win
    def check_diagonals(self):
        if (self._board[0][0] == self._board[1][1] == self._board[2][2]) \
                or (self._board[0][2] == self._board[1][1] == self._board[2][0]):  # /
            return True
        return False

    # Returns True if a winner is found or False otherwise
    def is_winner(self):
        return self.check_horizontals() or self.check_verticals() or self.check_diagonals()

    # Returns the board a string
    def get_board(self):
        board = '---------\n'
        for row in self._board:
            board += '| '
            for col in row:
                board += f"{col} "
            board += '|\n'
        board += '---------'
        return board


if __name__ == '__main__':
    game = TicTacToe()

    print('Welcome to Tic-Tac-Toe.')
    while game.get_state() == 'CONTINUE':
        print(game.get_board())
        print(f"Player {game.get_player()}, what's your move?")
        move_successful = False
        choice = input('Choose a number: ')
        while not move_successful:
            move_successful = game.make_move(choice)
            if not move_successful:
                choice = input('Please choose an available number: ')

    print(game.get_board())
    print(game.get_state())
