from Board import Board


class Bingo:

    def __init__(self):
        self.boards = []
        self.numbers = []

    def add_board(self, numbers):
        self.boards.append(Board(numbers))
        return True

    def check_boards_for_winners(self):
        winners = []
        for idx, board in enumerate(self.boards):
            if board.get_has_won() == False and board.check_for_win() == True:
                winners.append(idx)
        return winners

    def play_number(self, number):
        self.numbers.append(int(number))
        for board in self.boards:
            board.check_for_number(int(number))
        return True

    def get_board(self, number):
        return self.boards[number]

    def __len__(self):
        return len(self.boards)

    def __str__(self):
        s = ''
        for board in self.boards:
            s += str(board) + '\n'
        return s
