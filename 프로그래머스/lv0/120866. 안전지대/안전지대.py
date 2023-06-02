from collections import Counter
def solution(board):
    rows = len(board)
    cols = len(board)
    new_arr = [[0] * (cols + 2) for _ in range(rows + 2)]
    #테두리 = 1
    for i in range(len(new_arr)):
        for j in range(len(new_arr)):
            if i == 0 or j == 0 or i == len(new_arr)-1 or j == len(new_arr)-1:
                new_arr[i][j] = 1
    #원래 배열 new배열에 넣기
    for i in range(rows):
        for j in range(cols):
            new_arr[i+1][j+1] = board[i][j]            
    for i in range(rows):
        for j in range(cols):
            if new_arr[i+1][j+1] == 1:
                if new_arr[(i+1)-1][(j+1)-1] != 1: new_arr[(i+1)-1][(j+1)-1] = 2
                if new_arr[(i+1)-1][(j+1)] !=1: new_arr[(i+1)-1][(j+1)] =2
                if new_arr[(i+1)-1][(j+1)+1] !=1 :new_arr[(i+1)-1][(j+1)+1] = 2
                if new_arr[(i+1)][(j+1)-1] != 1 :new_arr[(i+1)][(j+1)-1] = 2
                if new_arr[(i+1)][(j+1)+1] != 1 : new_arr[(i+1)][(j+1)+1] = 2
                if new_arr[(i+1)+1][(j+1)-1] != 1 : new_arr[(i+1)+1][(j+1)-1] = 2
                if new_arr[(i+1)+1][(j+1)] != 1 : new_arr[(i+1)+1][(j+1)] = 2
                if new_arr[(i+1)+1][(j+1)+1] != 1 :new_arr[(i+1)+1][(j+1)+1] = 2  
    cnt = 0
    for i in range(len(new_arr)):
        for j in range(len(new_arr)):
            if new_arr[i][j] == 0:
                cnt += 1
    return cnt