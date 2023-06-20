from collections import Counter
def solution(X, Y):
    answer = ''
    X = dict(Counter(X))
    Y = dict(Counter(Y))
    common_keys = list(set(X.keys()) & set(Y.keys()))
    if len(common_keys) == 0:
        return "-1"
    else:
        if len(common_keys) == 1 and common_keys[0] == "0":
            return "0"
        else:
            for i in list(common_keys):
                answer += i * min(X.get(i), Y.get(i))
    return "".join(sorted(answer, reverse=True))