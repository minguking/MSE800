"""Tic-tac-toe CLI game for two players."""


def create_board():
    """Return a new empty 3x3 board."""
    return [[" " for _ in range(3)] for _ in range(3)]


def display_board(board):
    """Print the current board state."""
    print("\n  1   2   3")
    for i, row in enumerate(board):
        print(f"{i + 1} " + " | ".join(row))
        if i < 2:
            print("  -----------")
    print()


def check_winner(board, mark):
    """Return True if the given mark has won."""
    for row in board:
        if all(cell == mark for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True

    if all(board[i][i] == mark for i in range(3)):
        return True
    if all(board[i][2 - i] == mark for i in range(3)):
        return True

    return False


def is_draw(board):
    """Return True if the board is full with no winner."""
    return all(board[r][c] != " " for r in range(3) for c in range(3))


def get_move(player, mark):
    """Prompt the player for a valid move and return (row, col)."""
    while True:
        try:
            raw = input(f"Player {player} ({mark}) - Enter row and column (e.g. 1 2): ")
            parts = raw.strip().split()
            if len(parts) != 2:
                raise ValueError("Please enter two numbers.")
            row, col = int(parts[0]) - 1, int(parts[1]) - 1
            if row not in range(3) or col not in range(3):
                raise ValueError("Numbers must be between 1 and 3.")
            return row, col
        except ValueError as err:
            print(f"Invalid input: {err}")


def play_game():
    """Run a single game of Tic-tac-toe."""
    board = create_board()
    players = [("1", "X"), ("2", "O")]
    turn = 0

    print("=== Tic-Tac-Toe ===")
    display_board(board)

    while True:
        player, mark = players[turn % 2]
        row, col = get_move(player, mark)

        if board[row][col] != " ":
            print("That cell is already taken. Try again.")
            continue

        board[row][col] = mark
        display_board(board)

        if check_winner(board, mark):
            print(f"Player {player} ({mark}) wins! Congratulations!")
            return

        if is_draw(board):
            print("It's a draw!")
            return

        turn += 1


def main():
    """Entry point: run the game and offer replay."""
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
