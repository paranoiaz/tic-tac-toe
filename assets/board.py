from assets.token import Token


class Board:
    __instance = None

    # singleton design pattern implementation
    def __init__(self, board_size: int):
        if Board.__instance != None:
            raise Exception("Board is already instantiated.")
        self.matrix = [[Token.TOKEN_EMPTY] * board_size for _ in range(board_size)]
        Board.__instance = self

    @staticmethod
    def get_instance():
        if Board.__instance == None:
            Board(3)
        return Board.__instance

    def print_board(self):
        counter = 1
        for array in self.matrix:
            print(" | ".join(array))
            if counter != len(self.matrix):
                print("-" * (len(self.matrix) * len(self.matrix)))
                counter += 1

    def place_move(self, position: int, value: str):
        row: int = position // 3
        column: int = position % 3
        self.matrix[row][column] = value

    def is_position_empty(self, position: int) -> bool:
        row: int = position // 3
        column: int = position % 3
        return self.matrix[row][column] == Token.TOKEN_EMPTY

    def check_full_board(self) -> bool:
        for array in self.matrix:
            if Token.TOKEN_EMPTY in array:
                return False

        return True

    def check_winner(self) -> Token:
        # check horizontal
        for array in self.matrix:
            if len(set(array)) == 1 and array[0] != Token.TOKEN_EMPTY:
                return array[0]

        # check vertical
        for y in range(len(self.matrix)):
            if self.matrix[0][y] == self.matrix[1][y] == self.matrix[2][y]:
                return self.matrix[0][y]

        # check left-to-right diagonal
        if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2]:
            return self.matrix[0][0]

        # check right-to-left diagonal
        if self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0]:
            return self.matrix[0][2]

        return Token.TOKEN_EMPTY
