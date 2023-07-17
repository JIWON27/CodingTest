def solution(people, limit):
    answer = 0
    people.sort()
    start = 0
    end = len(people)-1
    while True:
        if start > end:
            break
        elif people[start] + people[end] <= limit:
            start = start + 1    
        end = end - 1
        answer = answer + 1
    return answer