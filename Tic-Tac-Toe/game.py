import time

from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize an empty 3x3 board
        self.current_winner = None  # Keep track of the winner

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            print('-------------')

    @staticmethod
    def print_board_nums():
        # 1 | 2 | 3 etc. (tells us what number corresponds to what box)
        number_board = [[str(i + 1) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
            print('-------------')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check rows
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # Check columns
        column_ind = square % 3
        column = [self.board[column_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonals; but only if the square is an even number (0, 2, 4, 6, 8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def play(game, XPlayer, OPlayer, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'  # starting letter

    while game.empty_squares():
        if letter == 'O':
            square = OPlayer.get_move(game)
        else:
            square = XPlayer.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print(' ')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins')
                return letter

            letter = 'O' if letter == 'X' else 'X'

        time.sleep(.8)
    if print_game:
        print("It's a tie!!")


# Choose the players as you want
if __name__ == "__main__":
    XPlayer = HumanPlayer("X")
    OPlayer = GeniusComputerPlayer("O")
    t = TicTacToe()
    play(t, XPlayer, OPlayer, print_game=True)
