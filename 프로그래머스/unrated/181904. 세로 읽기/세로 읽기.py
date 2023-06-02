def solution(my_string, m, c):
    if m == 1:
        return my_string
    string = ''
    answer = [my_string[i:i+m] for i in range(0, len(my_string), m)]
    for i in answer:
        string += i[c-1]
    return string