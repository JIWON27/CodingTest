from collections import Counter
def solution(participant, completion):
    answer = ''
    participant = Counter(participant)
    completion = Counter(completion)
    for i in participant.items():
        if i not in completion.items():
            answer = i[0]
    return answer