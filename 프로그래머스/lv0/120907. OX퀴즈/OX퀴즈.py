def solution(quiz):
    answer = []
    num = 0
    result = 0
    for i in quiz:
        arr = [j for j in i.split()]
        result = int(arr[-1])
        if arr[1] == '+':
            num = int(arr[0]) + int(arr[2])
        elif arr[1] == "-":
            num = int(arr[0]) - int(arr[2])
            
        if num == result :
            answer.append("O")
        else:
            answer.append("X")
    return answer