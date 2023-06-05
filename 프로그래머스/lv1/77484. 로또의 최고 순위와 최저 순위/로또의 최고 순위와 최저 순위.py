def solution(lottos, win_nums):
    rank = {"0":6, "1": 6, "2": 5, "3": 4, "4": 3, "5": 2, "6": 1}
    cnt = 0
    zero = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
        if i == 0:
            zero += 1
    return [rank[str(cnt+zero)],rank[str(cnt)]]