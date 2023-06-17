def solution(n):
    answer = [[0] * n for _ in range(n)]
    counter = 1
    pos_x = 0
    pos_y = 0
    Direction="right"
    while counter <= n**2:
        answer[pos_x][pos_y]=counter
        if Direction == "right":       
            if pos_y + 1 == n or answer[pos_x][pos_y+1] != 0:
                Direction = "down"
                pos_x += 1          
            else:       
                pos_y += 1
        elif Direction == "down":
            if pos_x + 1  == n or answer[pos_x + 1][pos_y] != 0:
                Direction = "left"
                pos_y -= 1
            else:          
                pos_x += 1
        elif Direction == "left":
            if pos_y - 1 < 0 or answer[pos_x][pos_y-1] != 0:        
                Direction = "up"
                pos_x -= 1
            else:
                pos_y -= 1

        elif Direction == "up":
            if pos_x - 1 < 0 or answer[pos_x-1][pos_y] != 0:           
                Direction = "right"
                pos_y += 1         
            else:           
                pos_x -= 1
        counter += 1
    return answer
