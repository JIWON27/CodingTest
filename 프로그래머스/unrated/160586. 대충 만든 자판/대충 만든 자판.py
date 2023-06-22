def solution(keymap, targets):
    answer = []
    for target in targets:
        cnt = 0
        for ch in target:
            idx = []
            for key in keymap:
                idx.append(key.find(ch))
                
            while -1 in idx:
                idx.remove(-1)
                
            if len(idx) == 0:
                cnt = -1
                break
            else:
                cnt += min(idx)+1
                
        answer.append(cnt)
    return answer