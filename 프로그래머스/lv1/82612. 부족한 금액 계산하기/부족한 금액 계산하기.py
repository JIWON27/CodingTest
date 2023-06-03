def solution(price, money, count):
    return  0 if price * (sum(range(1, count+1))) - money < 0 else price * (sum(range(1, count+1))) - money