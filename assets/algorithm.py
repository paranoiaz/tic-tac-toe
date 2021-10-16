import math
import random

from assets.board import Board
from assets.token import Token


class Algorithm:

    def __init__(self, difficulty: str):
        self.difficulty = difficulty.upper()

    def execute_next_move(self, board: Board):
        if self.difficulty == "EASY":
            self.calculate_easy_move(board)
        if self.difficulty == "HARD":
            self.calculate_hard_move(board)

    def calculate_easy_move(self, board: Board):
        random_number = random.randint(0, 8)
        if board.is_position_empty(random_number):
            board.place_move(random_number, Token.TOKEN_O)
            return

        self.calculate_easy_move(board)

    def calculate_hard_move(self, board: Board):
        best_move = 0
        best_score = -math.inf

        for possible_move in range(0, 9):
            if board.is_position_empty(possible_move):
                board.place_move(possible_move, Token.TOKEN_O)
                score = self.run_mini_max(board, False)
                board.place_move(possible_move, Token.TOKEN_EMPTY)

                if score > best_score:
                    best_score = score
                    best_move = possible_move

        board.place_move(best_move, Token.TOKEN_O)

    def run_mini_max(self, board: Board, is_maximizing: bool):
        if board.check_winner() == Token.TOKEN_O:
            return 1
        if board.check_winner() == Token.TOKEN_X:
            return -1
        if board.check_full_board():
            return 0

        if is_maximizing:
            best_score = -math.inf

            for move in range(0, 9):
                if board.is_position_empty(move):
                    # bot token
                    board.place_move(move, Token.TOKEN_O)
                    score = self.run_mini_max(board, False)
                    board.place_move(move, Token.TOKEN_EMPTY)

                    if score > best_score:
                        best_score = score

            return best_score

        else:
            worst_score = math.inf

            for move in range(0, 9):
                if board.is_position_empty(move):
                    # player token
                    board.place_move(move, Token.TOKEN_X)
                    score = self.run_mini_max(board, True)
                    board.place_move(move, Token.TOKEN_EMPTY)

                    if score < worst_score:
                        worst_score = score

            return worst_score
