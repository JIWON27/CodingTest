import re
def solution(phone_number):
    Regex = re.compile(r'(.{4})$')
    answer = re.findall(Regex,phone_number)
    return '*'*(len(phone_number)-4) + str(answer[0])