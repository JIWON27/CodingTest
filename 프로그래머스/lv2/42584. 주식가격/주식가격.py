
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices :
        price = prices.popleft()
        cnt = 0
        for value in prices:
            cnt += 1
            if value < price:   
                break;
        answer.append(cnt)            
    return answer