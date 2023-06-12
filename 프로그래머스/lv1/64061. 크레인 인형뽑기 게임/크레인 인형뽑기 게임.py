def solution(board, moves):
    # 숫자가 인형의 종류
    answer = 0
    stk = []
    for i in moves:
        for j in range(len(board[i-1])):
            if board[j][i-1] !=0:
                stk.append(board[j][i-1]) # 인형을 뽑아서 stk에 추가
                board[j][i-1] = 0 # 인형 뽑았으니 0으로
                break
            else:
                continue
    store = [0]
    while len(stk) != 0:
        pop_ = stk.pop()
        if store[-1] == pop_:
            store.pop()
            answer += 2
        else:
            store.append(pop_)
    return answer