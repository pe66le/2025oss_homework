import random

# 보드 초기화
board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")

def check_winner(player):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def player_move():
    while True:
        move = int(input("위치 선택 (0-8): "))
        if 0 <= move <= 8 and board[move] == " ":
            board[move] = "X"
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

def computer_move():
    available_moves = [i for i in range(9) if board[i] == " "]
    move = random.choice(available_moves)
    board[move] = "O"

def play_game():
    print_board()
    for turn in range(9):
        if turn % 2 == 0:
            print("\n당신의 차례(X)")
            player_move()
        else:
            print("\n컴퓨터의 차례(O)")
            computer_move()
        print_board()

        if check_winner("X"):
            print("당신이 승리했습니다!")
            return
        elif check_winner("O"):
            print("컴퓨터가 승리했습니다!")
            return

    print("무승부입니다!")

play_game()