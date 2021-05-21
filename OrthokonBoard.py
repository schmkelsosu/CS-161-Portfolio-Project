# Author: Kelsey Schmidt
# Date: 5-20-21
# Description:  # Creates a class called OrthokonBoard that represents the board
                # for a two-player game that is played on a 4x4 grid.
                # This class does not do everything needed to play a game
                # - it's just responsible for handling the rules concerning the game board.
                # The board starts with four red pieces on row 0 and four yellow pieces on row 3.
                # A valid move consists of a player moving one of their pieces orthogonally or diagonally
                # as far as it can go until it hits another piece or the edge of the board
                # (it must move at least one space).
                # After the piece stops, any opponent pieces on orthogonally adjacent squares
                # are flipped over to its color.
                # The OrthokonBoard class doesn't keep track of whose turn it is,
                # so it will allow multiple moves by the same player consecutively.
                # A player wins upon making a move that either flips over
                # the remaining opponent pieces or leaves the opponent without a move.

class OrthokonBoard:
    """
    Creates a class called OrthokonBoard that represents the board
    for a two-player game that is played on a 4x4 grid.
    This class does not do everything needed to play a game
    - it's just responsible for handling the rules concerning the game board.
    The board starts with four Red pieces (R) on row 0 and four Yellow pieces (Y) on row 3.
    A valid move consists of a player moving one of their pieces orthogonally or diagonally
    as far as it can go until it hits another piece or the edge of the board
    (it must move at least one space).
    After the piece stops, any opponent pieces on orthogonally adjacent squares
    are flipped over to its color.
    The OrthokonBoard class doesn't keep track of whose turn it is,
    so it will allow multiple moves by the same player consecutively.
    A player wins upon making a move that either flips over
    the remaining opponent pieces or leaves the opponent without a move.
    The class has private data members for:
            1. a representation of the board (4 lists within a list)
            2. the current state, which holds one of the three following values:
                "RED_WON", "YELLOW_WON", or "UNFINISHED"
    The class includes the following methods:
        1. An init method that takes no parameters,
            initializes the starting board positions,
            and initializes the current state to "UNFINISHED"
        2. A method named print_board that prints out the board.
            (Does not return anything, print function is within the method)
        3. A get method named get_current_state, which returns the current state.
        4. A method named make_move that takes four parameters (in the specific order listed):
                A. The row of the piece being moved
                B. The column of the piece being moved
                C. The row of the intended position that piece will be moved to
                D. The column f the intended position that piece will be moved to
        Rows are numbered from top to bottom (0, 1, 2, 3),
        Columns are numbered from left to right (0, 1, 2, 3)
        If the game has already been won, or if the move is not valid,
        make_move will return False.
        Otherwise, it will record the move, update the board,
        update the current state if the move caused a win, and return True.
    """

    def __init__(self):
        self._board = [[".","Y",".","."],[".",".",".","."],[".",".",".","."],[".",".",".","."]]
        self._current_state = "UNFINISHED"  # the default state of the game with no moves made is "UNFINISHED"

    def get_current_state(self):        # get method to get the current game state (Who won?)
        return self._current_state      # returns "RED_WON", "YELLOW_WON", or "UNFINISHED"

    def print_board(self):              # prints the board in a pretty fashion
        print("_" * 11)
        for line in self._board:
            print("|", *line[:], "|")
        print("‾" * 11)

    def make_move(self, piece_row, piece_column, position_row, position_column):    # method to make each move

        if self._current_state != "UNFINISHED":     # if the game state is anything but "UNFINISHED"
            print("The game is already over")
            return False                            # returns False, as the current game is already over

        if (piece_row or piece_column or position_row or position_column) not in range(0,4):
                                            # if any of the piece or position values are not 0-3 (not valid positions)
            print("Not a valid board position")
            return False                    # returns False, and a new valid move must be made

        valid_moves = []
        column_int = ""
        row_int = ""

        for int in range(piece_column + 1):  # check to the left of piece for valid move in that direction
            if piece_column == 0:
                break
            print("curr int:", int)
            if int == 0:
                continue
            if self._board[piece_row][piece_column - int] == ".":
                print("checking left coordinates")
                print(piece_row, piece_column - int)
                column_int = piece_column - int
                print("current valid left space", piece_row, column_int)
                continue
            else:
                break
        if column_int != "":
            valid_moves.append((piece_row, column_int))
            print("current valid moves:", valid_moves)
            column_int = ""

        for int in range(4 - piece_column):  # check to the right of piece for valid move in that direction
            if piece_column == 3:
                break
            print("curr int:", int)
            if int == 0:
                continue
            if self._board[piece_row][piece_column + int] == ".":
                print("checking right coordinates")
                print(piece_row, piece_column + int)
                column_int = piece_column + int
                print("current valid right space", piece_row, column_int)
                continue
            else:
                break
        if column_int != "":
            valid_moves.append((piece_row, column_int))
            print("current valid moves:", valid_moves)
            column_int = ""

        for int in range(piece_row + 1):  # check upwards of piece for valid move in that direction
            if piece_row == 0:
                break
            print("curr int:", int)
            if int == 0:
                continue
            if self._board[piece_row - int][piece_column] == ".":
                print("checking up coordinates")
                print(piece_row - int, piece_column)
                row_int = piece_row - int
                print("current valid up space", row_int, piece_column)
                continue
            else:
                break
        if row_int != "":
            valid_moves.append((row_int, piece_column))
            print("current valid moves:", valid_moves)
            row_int = ""

        for int in range(4 - piece_row):  # check downwards of piece for valid move in that direction
            if piece_row == 3:
                break
            print("curr int:", int)
            if int == 0:
                continue
            if self._board[piece_row + int][piece_column] == ".":
                print("checking down coordinates")
                print(piece_row + int, piece_column)
                row_int = piece_row + int
                print("current valid down space", row_int, piece_column)
                continue
            else:
                break
        if row_int != "":
            valid_moves.append((row_int, piece_column))
            print("current valid moves:", valid_moves)
            row_int = ""

        for int in range(piece_row + 1):  # check diag-up-left of piece for valid move in that direction
            print("curr int:", int)
            if piece_row == 0:
                break
            if piece_column == 0:
                break
            if int == 0:
                continue
            if self._board[piece_row - int][piece_column - int] == ".":
                print("checking diag-up-left coordinates")
                print(piece_row - int, piece_column - int)
                row_int = piece_row - int
                column_int = piece_column - int
                print("current valid diag-up-left space", row_int, column_int)
                continue
            else:
                break
        if row_int != "":
            valid_moves.append((row_int, column_int))
            print("current valid moves:", valid_moves)
            row_int = ""
            column_int = ""

        for int in range(4 - piece_column):  # check diag-down-right of piece for valid move in that direction
            if piece_row == 3:
                break
            if piece_column == 3:
                break
            print("curr int:", int)
            if piece_column == 3:
                break
            if int == 0:
                continue
            if self._board[piece_row + int][piece_column + int] == ".":
                print("checking diag-down-right coordinates")
                print(piece_row + int, piece_column + int)
                row_int = piece_row + int
                column_int = piece_column + int
                print("current valid diag-down-right space", row_int, column_int)
                continue
            else:
                break
        if row_int != "":
            valid_moves.append((row_int, column_int))
            print("current valid moves:", valid_moves)
            row_int = ""
            column_int = ""

        for int in range(piece_row + 1):  # check diag-up-right of piece for valid move in that direction
            print("curr int:", int)
            if piece_row == 0:
                break
            if piece_column == 3:
                break
            if int == 0:
                continue
            if self._board[piece_row - int][piece_column + int] == ".":
                print("checking diag-up-right coordinates")
                print(piece_row - int, piece_column + int)
                row_int = piece_row - int
                column_int = piece_column + int
                print("current valid diag-up-right space", row_int, column_int)
                continue
            else:
                break
        if row_int != "":
            valid_moves.append((row_int, column_int))
            print("current valid moves:", valid_moves)
            row_int = ""
            column_int = ""

        for int in range(4 - piece_column):  # check diag-down-left of piece for valid move in that direction
            print("curr int:", int)
            if piece_row == 3:
                break
            if piece_column == 0:
                break
            if int == 0:
                continue
            if self._board[piece_row + int][piece_column - int] == ".":
                print("checking diag-down-left coordinates")
                print(piece_row + int, piece_column - int)
                row_int = piece_row + int
                column_int = piece_column - int
                print("current valid diag-down-left space", row_int, column_int)
                continue
            else:
                break
        if row_int != "":
            valid_moves.append((row_int, column_int))
            print("current valid moves:", valid_moves)
            row_int = ""
            column_int = ""

        if (position_row,position_column) not in valid_moves :  # check if intended move is valid
            print("Move is not valid!")
            return False

        print("Move is valid!")

        if self._board[piece_row][piece_column] == "Y":
            self._board[position_row][position_column] = "Y"
            self._board[piece_row][piece_column] = "."
            if position_column > 0:  # check left for piece to change
                if self._board[position_row][position_column - 1] != ".":
                    self._board[position_row][position_column - 1] = "Y"
            if position_column < 3:  # check right for piece to change
                if self._board[position_row][position_column + 1] != ".":
                    self._board[position_row][position_column + 1] = "Y"
            if position_row > 0:  # check up for piece to change
                if self._board[position_row - 1][position_column] != ".":
                    self._board[position_row - 1][position_column] = "Y"
            if position_row < 3:  # check down for piece to change
                if self._board[position_row + 1][position_column] != ".":
                    self._board[position_row + 1][position_column] = "Y"
        if self._board[piece_row][piece_column] == "R":
            self._board[position_row][position_column] = "R"
            self._board[piece_row][piece_column] = "."
            if position_column > 0:  # check left for piece to change
                if self._board[position_row][position_column - 1] != ".":
                    self._board[position_row][position_column - 1] = "R"
            if position_column < 3:  # check right for piece to change
                if self._board[position_row][position_column + 1] != ".":
                    self._board[position_row][position_column + 1] = "R"
            if position_row > 0:  # check up for piece to change
                if self._board[position_row - 1][position_column] != ".":
                    self._board[position_row - 1][position_column] = "R"
            if position_row < 3:  # check down for piece to change
                if self._board[position_row + 1][position_column] != ".":
                    self._board[position_row + 1][position_column] = "R"

        for row in self._board:
            if "R" not in row:
                continue
            else:
                print("R in row")
                break
            self._current_state = "YELLOW_WON"
            return True
        for row in self._board:
            if "Y" not in row:
                continue
            else:
                print("Y in row")
                break
            self._current_state = "RED_WON"
            return True

        red_list = []
        yellow_list = []

        for row in range(4) :
            for column in range(4) :
                if self._board[row][column] == "." :
                    continue
                if self._board[row][column] == "R" :
                    red_list.append((row,column))
                elif self._board[row][column] == "Y" :
                    yellow_list.append((row,column))

        print(red_list)








        # self._board[piece_row][piece_column]
        # self._board[position_row][position_column]



board = OrthokonBoard()
board.print_board()
board.make_move(0,1,3,1)
board.print_board()
print(board.get_current_state())

