def solution(s, skip, index):
    skip = [ord(i) for i in skip]
    answer = ''
    for i in s:
        count = 0
        num = ord(i)
        idx = 1
        while count != index:
            if num+idx > 122:
                num -=26
            if num + idx not in skip:
                num = num + idx
                count += 1
                idx = 1
            else:
                idx += 1
        answer += chr(num)
    return answer