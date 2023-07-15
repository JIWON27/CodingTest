def solution(wallpaper):
    answer_x = []
    answer_y = []
    answer = []
    
    x = 0
    for paper in wallpaper:
        for j in range(len(paper)):
            if paper[j] == '#':
                answer_x.append(x)
                answer_y.append(j)
        x += 1
        
    answer.append(min(answer_x))
    answer.append(min(answer_y))
    answer.append(max(answer_x)+1)
    answer.append(max(answer_y)+1)
    return answer