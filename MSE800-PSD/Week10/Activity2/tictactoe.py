"""Tic-tac-toe CLI game for two players."""


class TicTacToe:
    """Manages the board state and game logic for a Tic-tac-toe game."""

    def __init__(self):
        """Initialise an empty board and set up for two players."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = [("1", "X"), ("2", "O")]
        self.turn = 0

    @property
    def current_player(self):
        """Return the (player_number, mark) tuple for the current turn."""
        return self.players[self.turn % 2]

    def display(self):
        """Print the current board state."""
        print("\n  1   2   3")
        for i, row in enumerate(self.board):
            print(f"{i + 1} " + " | ".join(row))
            if i < 2:
                print("  -----------")
        print()

    def is_winner(self, mark):
        """Return True if the given mark has won."""
        board = self.board

        if any(all(cell == mark for cell in row) for row in board):
            return True

        if any(all(board[r][c] == mark for r in range(3)) for c in range(3)):
            return True

        if all(board[i][i] == mark for i in range(3)):
            return True

        if all(board[i][2 - i] == mark for i in range(3)):
            return True

        return False

    def is_draw(self):
        """Return True if the board is full with no winner."""
        return all(self.board[r][c] != " " for r in range(3) for c in range(3))

    def get_move(self):
        """Prompt the current player for a valid move and return (row, col)."""
        player, mark = self.current_player
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

    def make_move(self, row, col):
        """Place the current player's mark on the board.

        Return False if the cell is already occupied.
        """
        if self.board[row][col] != " ":
            return False
        _, mark = self.current_player
        self.board[row][col] = mark
        return True

    def play(self):
        """Run a single game loop until there is a winner or a draw."""
        print("=== Tic-Tac-Toe ===")
        self.display()

        while True:
            player, mark = self.current_player
            row, col = self.get_move()

            if not self.make_move(row, col):
                print("That cell is already taken. Try again.")
                continue

            self.display()

            if self.is_winner(mark):
                print(f"Player {player} ({mark}) wins! Congratulations!")
                return

            if self.is_draw():
                print("It's a draw!")
                return

            self.turn += 1


def main():
    """Entry point: run the game and offer replay."""
    while True:
        game = TicTacToe()
        game.play()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
