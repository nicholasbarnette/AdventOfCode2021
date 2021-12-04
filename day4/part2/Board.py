import math


class Cell:
    checked = False

    def __init__(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def get_checked(self):
        return self.checked

    def set_checked(self):
        self.checked = True
        return True

    def __str__(self):
        return str(self.number) + ("_" if self.checked == True else "")


class Board:
    rows = columns = 5
    has_won = False

    def __init__(self, numbers):
        self.board = [[None for col in range(
            self.columns)] for row in range(self.rows)]
        for idx, number in enumerate(numbers):
            i = math.floor(idx / self.rows)
            j = idx % self.columns
            self.board[i][j] = Cell(int(number))
        return

    def check_for_win(self):
        # Check horizontally
        for i in range(self.rows):
            checked_columns = 0
            for j in range(self.columns):
                if self.board[i][j].get_checked() == True:
                    checked_columns += 1
            if checked_columns == self.columns:
                self.has_won = True
                return True

        # Check vertically
        for j in range(self.columns):
            checked_rows = 0
            for i in range(self.rows):
                if self.board[i][j].get_checked() == True:
                    checked_rows += 1
            if checked_rows == self.columns:
                self.has_won = True
                return True

        return False

    def check_for_number(self, number):
        if self.has_won == True:
            return
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j].get_number() == number:
                    self.board[i][j].set_checked()

    def handle_numbers(self, numbers):
        if self.has_won == True:
            return
        for number in numbers:
            self.check_for_number(number)

    def get_cells(self):
        cells = []
        for i in range(self.rows):
            for j in range(self.columns):
                cells.append(self.board[i][j])
        return cells

    def get_has_won(self):
        return self.has_won

    def __str__(self):
        s = ""
        for i in range(self.rows):
            for j in range(self.columns):
                s += str(self.board[i][j]) + "\t"
            s += '\n'
        return s
