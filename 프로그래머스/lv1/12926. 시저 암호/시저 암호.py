def solution(s, n):
    answer = ''
    for i in s:
        if i.isalpha(): 
            if 65 <= ord(i) <= 90:
                if 90 < ord(i)+n:
                    answer += chr(ord(i)+n-26)
                else:
                    answer += chr(ord(i)+n) 
            elif 97 <= ord(i) <= 122:
                if 122 < ord(i)+n:
                    answer += chr(ord(i)+n-26)
                else:
                    answer += chr(ord(i)+n) 
        else:
            answer += ' '
    return answer