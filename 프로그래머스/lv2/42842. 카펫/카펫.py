def solution(brown, yellow):
    answer = []
    if yellow == 1:
        return [3,3]
    else:
        number = yellow
        while True:
            if yellow % number == 0: # 약수면
                print( 2 * (number + 2 + (yellow // number))) 
                if  2 * (number + 2 + (yellow // number)) == brown:
                    break;
            number -= 1
    return [number+2, yellow // number+2]