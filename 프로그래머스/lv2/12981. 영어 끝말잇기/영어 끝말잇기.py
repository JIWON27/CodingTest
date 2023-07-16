def solution(n, words):
    answer = []
    
    for i in range(0,len(words),n): 
        # 앞에 나왔던 단어를 말한 경우
        for j in range(i, min(i+n, len(words))):
            if words[j] in words[:j]:
                answer.append(j%n+1)
                answer.append(j//n+1)
                return answer
        # 이전 글자의 끝 글자로 시작하지 않는 경우
        for j in range(i+1, min(i+1+n, len(words))): 
            before = words[j-1]
            if not words[j].startswith(before[-1]) :
                answer.append(j%n+1)
                answer.append(j//n+1)
                return answer
    return [0,0]