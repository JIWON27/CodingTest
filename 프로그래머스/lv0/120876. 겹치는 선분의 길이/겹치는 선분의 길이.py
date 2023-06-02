def solution(lines):
    total = 0
    num_list = [0 for _ in range(200)]
    for i in lines:
        for j in range(i[0]+100,i[1]+100):
            num_list[j] += 1
    for i in num_list:
        if i >= 2:
            total += 1
    return total