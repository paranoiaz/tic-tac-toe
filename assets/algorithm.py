import math
import random

from board import Board
from token import Token


class Algorithm:

    def __init__(self, difficulty: str):
        self.difficulty = difficulty

    def next_move(self, board: Board):
        if self.difficulty == "EASY":
            self.calculate_easy_move(board)
        if self.difficulty == "HARD":
            self.calculate_hard_move(board)

    def calculate_easy_move(self, board: Board):
        random_number = random.randint(1, 9)

        if board.is_position_empty(random_number - 1):
            board.place_move(random_number - 1, Token.TOKEN_O)
            return

        self.calculate_easy_move(board)

    def calculate_hard_move(self, board: Board):
        best_move = 0
        best_score = -math.inf

        for move in range(1, 10):
            if board.is_position_empty(move - 1):
                board.place_move(move - 1, Token.TOKEN_O)
                score = self.run_mini_max(board, False)
                board.place_move(move - 1, Token.TOKEN_EMPTY)

                if score > best_score:
                    best_score = score
                    best_move = move

        board.place_move(best_move - 1, Token.TOKEN_O)

    def run_mini_max(self, board: Board, is_maximizing):
        if board.check_winner() == Token.TOKEN_O:
            return 1

        if board.check_winner() == Token.TOKEN_X:
            return -1

        if board.check_full_board():
            return 0

        if is_maximizing:
            best_score = -math.inf

            for move in range(1, 10):
                if board.is_position_empty(move - 1):
                    board.place_move(move - 1, Token.TOKEN_O)
                    score = self.run_mini_max(board, False)
                    board.place_move(move - 1, Token.TOKEN_EMPTY)

                    if score > best_score:
                        best_score = score

            return best_score

        else:
            best_score = math.inf

            for move in range(1, 10):
                if board.is_position_empty(move - 1):
                    board.place_move(move - 1, Token.TOKEN_X)
                    score = self.run_mini_max(board, True)
                    board.place_move(move - 1, Token.TOKEN_EMPTY)

                    if score < best_score:
                        best_score = score

            return best_score