def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    sizes = sorted(sizes, key=lambda x:x[0])
    w_max = sizes[len(sizes)-1][0]
    sizes = sorted(sizes, key=lambda x:x[1])
    h_max = sizes[len(sizes)-1][1]
    return w_max * h_max

# def solution(sizes):
#   w_max = 0
#   h_max = 0
#   for i in range(len(sizes)):
#       if sizes[i][0] < sizes[i][1]:
#           sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
#       w_max = max(w_max,sizes[i][0] )
#       h_max = max(h_max,sizes[i][1] )
#   return w_max * h_max 
