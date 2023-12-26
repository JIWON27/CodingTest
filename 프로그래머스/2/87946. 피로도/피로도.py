from itertools import permutations
def solution(k, dungeons):
    count = [] 
    all_dungeons = permutations(dungeons)

    for dungeons in list(all_dungeons):
        cnt = 0
        copy_k = k
        for dungeon in dungeons:
            if dungeon[0] <= copy_k: # 80 <= 80
                cnt += 1
                copy_k -= dungeon[1] # 80 - 20 = 60
        count.append(cnt)
    return max(count)