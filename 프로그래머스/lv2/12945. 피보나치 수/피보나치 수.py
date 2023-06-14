def solution(n):
    fibo = [0,1]
    idx = 2
    while True:
        if len(fibo) > n:
            if fibo[n] != 0:
                return fibo[n] % 1234567
        else:
            fibo.append(fibo[idx-1] + fibo[idx-2])
            idx += 1