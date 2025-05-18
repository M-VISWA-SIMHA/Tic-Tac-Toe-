def print_board(board):
    print("\n")
    print("   |   |")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("___|___|___")
    print("   |   |")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("___|___|___")
    print("   |   |")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("   |   |")
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_draw(board):
    return all(space in ['X', 'O'] for space in board)

def play_game():
    board = ['1','2','3','4','5','6','7','8','9']
    current_player = 'X'
    game_running = True

    while game_running:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ")

        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input. Please try again.")
            continue

        move = int(move) - 1

        if board[move] in ['X', 'O']:
            print("This cell is already taken. Choose another one.")
            continue

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            game_running = False
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            game_running = False
        else:
            current_player = 'O' if current_player == 'X' else 'X'

# Run the game
play_game()
