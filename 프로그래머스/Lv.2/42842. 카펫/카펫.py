def solution(brown, yellow):
    number = yellow
    while True:
        if yellow % number == 0: # 약수면
            if  2 * (number + 2 + (yellow // number)) == brown:
                break;
        number -= 1
    return [number+2, yellow // number+2]