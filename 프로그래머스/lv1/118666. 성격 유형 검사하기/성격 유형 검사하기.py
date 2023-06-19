def solution(survey, choices):
    answer = ''
    dict_ = {'R':0, 'T':0,'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for character,choice in zip(survey,choices):
        if 1<= choice <= 3:
            if choice == 1:
                dict_[character[0]] += 3
            elif choice == 2:
                dict_[character[0]] += 2
            else:
                dict_[character[0]] += 1
        elif 5 <= choice <= 7:
            dict_[character[1]] += choice-4
    cnt = 0
    curr = 0
    curr_char = ''
    for character, score in dict_.items():
        if cnt == 2 or cnt == 0:
            curr = score
            curr_char = character
            cnt = 0
        elif cnt == 1:
            if curr < score:
                answer += character
            else: 
                answer += curr_char
        cnt += 1
    return answer