import random


def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def is_draw(board):
    return all(space in ["X", "O"] for space in board)


def computer_move(board):
    available_spaces = [
        i for i in range(9)
        if board[i] not in ["X", "O"]
    ]

    return random.choice(available_spaces)


def play_game():
    board = [str(i) for i in range(1, 10)]

    print("🎮 Tic-Tac-Toe")
    print("You are X. The computer is O.")

    while True:
        # Player's turn
        print_board(board)

        choice = input("Choose a space (1-9): ")

        if not choice.isdigit() or int(choice) not in range(1, 10):
            print("Please enter a number from 1 to 9.")
            continue

        position = int(choice) - 1

        if board[position] in ["X", "O"]:
            print("That space is already taken.")
            continue

        board[position] = "X"

        if check_winner(board, "X"):
            print_board(board)
            print("🎉 You win!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Computer's turn
        position = computer_move(board)
        board[position] = "O"

        print(f"The computer chose space {position + 1}.")

        if check_winner(board, "O"):
            print_board(board)
            print("🤖 The computer wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break


play_game()
