def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = (numer1 * denom2) + (numer2 * denom1)
    denom = denom1 * denom2
    num = numer
    de = denom
    gcd = 0
    while denom > 0:
        numer, denom = denom, numer % denom
    gcd = numer
    answer = [num//gcd, de//gcd]
    return answer