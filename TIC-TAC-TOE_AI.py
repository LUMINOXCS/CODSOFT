#TIC-TAC-TOE AI                                                                                                                                                                                                         import math
import math
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False


def evaluate(board):
    
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] == 'X':
                return 10
            elif row[0] == 'O':
                return -10

    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10

    
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10

    
    return 0


def minimax(board, depth, is_max, alpha, beta):
    score = evaluate(board)

    
    if score == 10:
        return score - depth

  
    if score == -10:
        return score + depth

    
    if not is_moves_left(board):
        return 0

    
    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_max, alpha, beta))
                    board[i][j] = " "
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_max, alpha, beta))
                    board[i][j] = " "
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best


def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = 'X'
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move


def check_winner(board):
    score = evaluate(board)
    if score == 10:
        return "AI wins!"
    elif score == -10:
        return "You win!"
    elif not is_moves_left(board):
        return "It's a tie!"
    return None


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
       
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] == " ":
                    board[row][col] = 'O'
                    break
                else:
                    print("Cell already taken, choose another.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter numbers between 0 and 2.")

        print_board(board)
        winner = check_winner(board)
        if winner:
            print(winner)
            break

        
        print("AI's move:")
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = 'X'
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(winner)
            break

if __name__ == "__main__":
    main()
