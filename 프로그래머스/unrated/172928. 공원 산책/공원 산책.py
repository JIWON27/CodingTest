def solution(park, routes):
    start = []
    
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                start.append(i)
                start.append(j)
                break;
    
    for route in routes:
        if route[0] == 'N': # 위로
            if start[0] - int(route[2]) >= 0 : 
                cnt = start[0]
                check = True
                for row in park[start[0]::-1]:
                    if cnt == start[0] - int(route[2])-1: 
                        break
                    else:
                        if row[start[1]] == 'X':
                            check = False
                    cnt -= 1
                if check:
                    start[0] -= int(route[2])
           # print(start[0], start[1])
        elif route[0] == 'S': # 아래
            if start[0] + int(route[2]) < len(park) : 
                cnt = start[0]
                check = True
                for row in park[start[0]:] :
                    if cnt == start[0] + int(route[2])+1: 
                        break
                    else:
                        if row[start[1]] == 'X':
                            check = False
                    cnt += 1
                if check:
                    start[0] += int(route[2])
            #print(start[0], start[1])
        elif route[0] == 'W': # 왼쪽
            if start[1] - int(route[2]) >= 0: 
                cnt = start[1]
                check = True
                for col in park[start[0]][start[1]::-1]:
                    if cnt == start[1] - int(route[2])-1: 
                        break
                    else:
                        if col == 'X':
                            check = False
                    cnt -= 1
                if check:
                    start[1] -= int(route[2])
            #print(start[0], start[1])
        else: # route[0] == 'E' # 오른쪽
            if start[1] + int(route[2]) < len(park[0]) : 
                cnt = start[1]
                check = True
                for col in park[start[0]][start[1]::]:
                    if cnt == start[1] + int(route[2])+1: 
                        break
                    else:
                        if col == 'X':
                            check = False
                    cnt += 1
                if check:
                    start[1] += int(route[2])
           # print(start[0], start[1])
    return start