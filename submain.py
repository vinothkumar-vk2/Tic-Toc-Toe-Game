import math
def print_board(board):
    print(board[0],"|",board[1],"|",board[2],"|",
        board[3],"|",board[4],"|",board[5],"|",
        board[6],"|",board[7],"|",board[8])
          
def check_winner(board,player):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    for combo in wins:
        if all(board[i]==player for i in combo):
            return True
    return False


def draw_s(board):
    return " " not in board


def min_max_algo(board,is_maxi):
    if check_winner(board,"O"):
        return 1
    if check_winner(board,"X"):
        return -1

    if draw_s(board):
        return 0
    

    if is_maxi:
        best_score=-1000

        for i in range(9):

            if board[i]=="":
                board[i]="X"
                score=min_max_algo(board,False)
                board[i]=""
                best_score=max(score,best_score)
        return best_score

def ai_move(board):

    best_score=-math.inf
    move=-1

    for i in range(9):
        if board[i]=="":
            board[i]="O"
            score=min_max_algo(board,True)
            board[i]=""


            if score>best_score:
                best_score=score
                move=i
    board[move]="O"
    return board