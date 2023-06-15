def solution(numbers, hand):
    answer = ''
    left = ['*']
    right = ['#']
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            left.append(i) 
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            right.append(i)
        else: # 2,5,8,0 
            disL=0
            disR=0
            if i == 2:
                dis_mapping = {1:1, 4:2, 7:3, '*':4, 3:1, 6:2, 9:3, '#':4, 2:0, 5:1, 8:2, 0:3}
                disL = dis_mapping.get(left[-1])
                disR = dis_mapping.get(right[-1])
            elif i == 5:
                dis_mapping = {1:2, 4:1, 7:2, '*':3, 3:2, 6:1, 9:2, '#':3, 2:1, 5:0, 8:1, 0:2}
                
                disL = dis_mapping.get(left[-1])
                disR = dis_mapping.get(right[-1])
            elif i == 8:
                dis_mapping = {1:3, 4:2, 7:1, '*':2, 2:2, 3:3, 6:2, 9:1, '#':2, 5:1, 8:0, 0:1}
                disL = dis_mapping.get(left[-1])
                disR = dis_mapping.get(right[-1])
            else: # i == 0
                dis_mapping = {1:4, 4:3, 7:2, '*':1, 3:4, 6:3, 9:2, '#':1, 2:3, 5:2, 8:1, 0:0}
                disL = dis_mapping.get(left[-1])
                disR = dis_mapping.get(right[-1])
                
            if disL > disR:
                answer += 'R'
                right.append(i)
            elif disL < disR:
                answer += 'L'
                left.append(i)
            elif disL == disR:
                if hand == 'left':
                    answer += 'L'
                    left.append(i)
                else:
                    answer += 'R'
                    right.append(i)
    return answer