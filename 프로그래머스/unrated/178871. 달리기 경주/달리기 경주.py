def solution(players, callings):
    Rank_1 = { name : idx+1  for idx,name in enumerate(players) }
    Rank_2 = { idx+1 : name  for idx,name in enumerate(players) }
    
    for call in callings:
        rank = Rank_1[call] 
        player = Rank_2[rank-1] 
        
        Rank_1[call] = rank-1
        Rank_2[rank-1] = call
        
        Rank_1[player] = rank 
        Rank_2[rank] = player
        
    Rank_1 = [i[0] for i in sorted(Rank_1.items(), key=lambda x: x[1])]
    return Rank_1