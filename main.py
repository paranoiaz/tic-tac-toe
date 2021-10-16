import os
import re
import yaml

from assets.algorithm import Algorithm
from assets.board import Board
from assets.token import Token


CONFIG = yaml.safe_load(open("config.yml", "r"))


def print_menu():
    print("Welcome to Tic Tac Toe\n\n"
          "1. Play vs player\n"
          "2. Play vs bot\n"
          "3. Settings\n")


def clear_screen():
    return os.system("cls") if os.name == "nt" else os.system("clear")


def check_input(player_input):
    return player_input.isdigit() and re.search("^[1-9]$", player_input)


def check_game_state(board):
    if board.check_full_board():
        clear_screen()
        board.print_board()
        print("\nThe game ended in a draw.")
        return False

    if board.check_winner() != Token.TOKEN_EMPTY:
        clear_screen()
        board.print_board()
        print(f"\nPlayer {board.check_winner()} has won the game.")
        return False

    return True


def play_vs_player():
    board = Board.get_instance()
    current_player = Token.TOKEN_X
    game_state = True

    while game_state:
        clear_screen()
        board.print_board()

        print(f"\nIt is {current_player}'s turn, choose a position to place it (1 - 9).\n")
        player_input = input("> ")

        if check_input(player_input):
            if board.is_position_empty(int(player_input) - 1):
                board.place_move(int(player_input) - 1, current_player)
                if current_player == Token.TOKEN_X:
                    current_player = Token.TOKEN_O
                else:
                    current_player = Token.TOKEN_X

        game_state = check_game_state(board)


def play_vs_bot():
    board = Board.get_instance()
    algorithm = Algorithm(CONFIG["difficulty"] or "EASY")
    game_state = True
    player_turn = True

    while game_state:
        clear_screen()
        board.print_board()

        if player_turn:
            print(f"\nIt is your turn, choose a position to place it (1 - 9).\n")
            player_input = input("> ")

            if check_input(player_input):
                if board.is_position_empty(int(player_input) - 1):
                    board.place_move(int(player_input) - 1, Token.TOKEN_X)
                    player_turn = False
        else:
            algorithm.execute_next_move(board)
            player_turn = True

        game_state = check_game_state(board)


def change_settings():
    clear_screen()
    print("Choose your difficulty:\n\n"
          "1. EASY\n"
          "2. HARD\n\n"
          f"Current difficulty: {CONFIG['difficulty'] or 'EASY'}\n")

    difficulty_input = input("> ")

    if difficulty_input.lower() == "1":
        CONFIG['difficulty'] = "EASY"
    if difficulty_input.lower() == "2":
        CONFIG['difficulty'] = "HARD"

    with open("config.yml", "w") as out:
        yaml.dump(CONFIG, out, default_flow_style=False)

    main()


def main():
    clear_screen()
    print_menu()

    input_choice = input("> ")

    if input_choice.lower() == "1":
        play_vs_player()
    elif input_choice.lower() == "2":
        play_vs_bot()
    elif input_choice.lower() == "3":
        change_settings()
    else:
        main()


if __name__ == "__main__":
    main()
