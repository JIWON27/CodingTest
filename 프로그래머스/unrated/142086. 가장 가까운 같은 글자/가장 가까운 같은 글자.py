def solution(s):
    answer = []
    for i in range(len(s)):
        index = 0
        if s[i] in s[:i]:
            index = s[:i].rfind(s[i])
            answer.append(i-index)
        else:
             answer.append(-1)
    return answer