import math
def solution(a, b):
    answer = 0
    num = math.gcd(a,b)
    b = b//num
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2