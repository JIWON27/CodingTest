
def solution(s):
    cnt = 0
    zero = 0
    while s != '1':
        if s == '1':
            return [0,0]
        else:
            length = len(s) - s.count('0')
            zero += s.count('0')
            s = bin(length)[2:]
            cnt += 1
    return [cnt, zero]