import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z-_.0-9]','',new_id)
    new_id = re.sub('[.]{2,}','.',new_id)
    new_id = re.sub('^[.]|[.]$','',new_id)
    if len(new_id) == 0:
        new_id = new_id.replace('','a')
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = re.sub('^[.]|[.]$','',new_id)
    if len(new_id) <= 2 :
        last_char = new_id[-1] 
        while len(new_id) < 3:
            new_id += last_char    
    return new_id