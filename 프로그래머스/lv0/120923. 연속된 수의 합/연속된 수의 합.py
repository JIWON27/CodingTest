def solution(num, total):
    answer = []
    m = (((total * 2) / num) + num - 1) / 2
    answer.append(m)
    for i in range(0,num-1):
        m = m-1
        answer.append(int(m))
    return sorted(answer)