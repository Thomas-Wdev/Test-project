# BATTLESHIP - 2 PLAYER GAME
# 10 columns x 8 rows
# Uses 2D lists (arrays)

ROWS = 8
COLUMNS = 10

SHIPS = {
    "Carrier": 4,
    "Destroyer": 3,
    "Submarine": 2
}


def create_board():
    """Create an empty 8x10 board."""
    return [["~" for _ in range(COLUMNS)] for _ in range(ROWS)]


def print_board(board, hide_ships=False):
    """Display a board."""

    print("\n     ", end="")

    for column in range(1, COLUMNS + 1):
        print(f"{column:2}", end=" ")

    print()
    print("    " + "---" * COLUMNS)

    for row in range(ROWS):
        print(chr(65 + row) + " | ", end="")

        for column in range(COLUMNS):
            cell = board[row][column]

            # Hide ships from the opponent
            if hide_ships and cell == "S":
                cell = "~"

            print(f"{cell:2}", end=" ")

        print()


def get_coordinate():
    """Get a coordinate such as A1, B5 or H10."""

    while True:

        coordinate = input(
            "Enter a coordinate (e.g. A1 or H10): "
        ).upper().strip()

        if len(coordinate) < 2 or len(coordinate) > 3:
            print("Invalid coordinate.")
            continue

        row_letter = coordinate[0]
        column_number = coordinate[1:]

        # Check row
        if row_letter not in "ABCDEFGH":
            print("Row must be A-H.")
            continue

        # Check column
        if not column_number.isdigit():
            print("Column must be a number.")
            continue

        column = int(column_number)

        if column < 1 or column > COLUMNS:
            print("Column must be between 1 and 10.")
            continue

        row = ord(row_letter) - ord("A")
        column -= 1

        return row, column


def place_ship(board, ship_name, ship_size):
    """Place a ship on the board."""

    print(f"\nPlace your {ship_name} ({ship_size} spaces).")
    print_board(board)

    while True:

        start_row, start_col = get_coordinate()

        direction = input(
            "Direction - R for right or D for down: "
        ).upper().strip()

        if direction not in ["R", "D"]:
            print("Please enter R or D.")
            continue

        # Calculate the final position
        if direction == "R":
            end_row = start_row
            end_col = start_col + ship_size - 1
        else:
            end_row = start_row + ship_size - 1
            end_col = start_col

        # Check whether the ship fits
        if end_row >= ROWS or end_col >= COLUMNS:
            print("That ship would go outside the board.")
            continue

        # Check for overlap
        valid = True

        for i in range(ship_size):

            if direction == "R":
                row = start_row
                col = start_col + i
            else:
                row = start_row + i
                col = start_col

            if board[row][col] != "~":
                valid = False

        if not valid:
            print("That ship overlaps another ship.")
            continue

        # Place the ship
        for i in range(ship_size):

            if direction == "R":
                row = start_row
                col = start_col + i
            else:
                row = start_row + i
                col = start_col

            board[row][col] = "S"

        print(f"{ship_name} placed!")
        break


def all_ships_destroyed(board):
    """Check whether all ships have been destroyed."""

    for row in board:
        if "S" in row:
            return False

    return True


def clear_screen():
    """
    Creates a visual barrier between players.

    This doesn't truly clear the terminal on every system,
    but printing many blank lines prevents the previous
    player's board from being immediately visible.
    """

    print("\n" * 40)


def pass_to_next_player(next_player):
    """
    Creates a blocker between turns so players
    cannot see each other's boards.
    """

    clear_screen()

    print("=" * 40)
    print("          PASS THE COMPUTER")
    print("=" * 40)

    print("\nGive the computer to the other player.")

    input("\nPress ENTER when you are ready...")

    clear_screen()

    print("=" * 40)
    print(f"          PLAYER {next_player}")
    print("=" * 40)


def take_turn(player_name, opponent_board):
    """
    Take one shot.

    Returns:
        True  = hit (player gets another turn)
        False = miss (turn changes)
    """

    print(f"\n{player_name}'s turn!")

    print("\nOpponent's board:")
    print_board(opponent_board, hide_ships=True)

    while True:

        row, col = get_coordinate()

        # Check if square was already attacked
        if opponent_board[row][col] == "X":
            print("You already hit that square.")
            continue

        if opponent_board[row][col] == "O":
            print("You already attacked that square.")
            continue

        # HIT
        if opponent_board[row][col] == "S":

            opponent_board[row][col] = "X"

            print("\n*** HIT! ***")
            print("You get another turn!")

            return True

        # MISS
        else:

            opponent_board[row][col] = "O"

            print("\nMISS!")

            return False


def main():

    # Create the two boards
    player1_board = create_board()
    player2_board = create_board()

    print("=" * 40)
    print("          BATTLESHIP")
    print("        2 PLAYER GAME")
    print("          10 x 8")
    print("=" * 40)

    # =================================
    # PLAYER 1 PLACES SHIPS
    # =================================

    print("\nPLAYER 1 - PLACE YOUR SHIPS")

    for ship_name, ship_size in SHIPS.items():
        place_ship(player1_board, ship_name, ship_size)

    print("\nYour final board:")
    print_board(player1_board)

    input("\nPress ENTER when Player 1 is finished...")

    # Hide Player 1's board
    clear_screen()

    # =================================
    # PLAYER 2 PLACES SHIPS
    # =================================

    print("PLAYER 2 - PLACE YOUR SHIPS")

    for ship_name, ship_size in SHIPS.items():
        place_ship(player2_board, ship_name, ship_size)

    print("\nYour final board:")
    print_board(player2_board)

    input("\nPress ENTER when Player 2 is finished...")

    # Hide Player 2's board
    clear_screen()

    print("=" * 40)
    print("          BATTLE BEGINS!")
    print("=" * 40)

    input("\nPress ENTER to let Player 1 start...")

    clear_screen()

    # Player 1 starts
    current_player = 1

    while True:

        # =================================
        # PLAYER 1'S TURN
        # =================================

        if current_player == 1:

            hit = take_turn(
                "Player 1",
                player2_board
            )

            # Check if Player 2 has lost
            if all_ships_destroyed(player2_board):

                print("\n" + "=" * 40)
                print("          PLAYER 1 WINS!")
                print("=" * 40)

                break

            # If Player 1 hit, they play again
            if hit:
                input("\nPress ENTER to continue your turn...")
                clear_screen()

            # If Player 1 missed, Player 2 gets the turn
            else:
                current_player = 2

                pass_to_next_player(2)

        # =================================
        # PLAYER 2'S TURN
        # =================================

        else:

            hit = take_turn(
                "Player 2",
                player1_board
            )

            # Check if Player 1 has lost
            if all_ships_destroyed(player1_board):

                print("\n" + "=" * 40)
                print("          PLAYER 2 WINS!")
                print("=" * 40)

                break

            # If Player 2 hit, they play again
            if hit:
                input("\nPress ENTER to continue your turn...")
                clear_screen()

            # If Player 2 missed, Player 1 gets the turn
            else:
                current_player = 1

                pass_to_next_player(1)


# Start the game
main()
