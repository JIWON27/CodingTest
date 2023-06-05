def solution(arr):
    answer = [[]]
    max_row = len(arr)
    max_col = 0
    for row in arr:
        col_count = len(row)  
        max_col = max(max_col, col_count) 
    if max_row > max_col:
        for idx in range(len(arr)):
            while len(arr[idx]) < max_row:
                arr[idx].append(0)
    else: # max_row < max_col   
        for _ in range(max_col-max_row):
            arr.append([0] * max_col)
    return arr