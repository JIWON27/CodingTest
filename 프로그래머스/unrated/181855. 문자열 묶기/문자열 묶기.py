from collections import Counter
def solution(strArr):
    answer = []
    for i in strArr:
        answer.append(len(i))
    cnt = Counter(answer).most_common(1)
    return (cnt[0])[1]