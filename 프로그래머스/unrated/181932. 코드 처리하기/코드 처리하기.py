def solution(code):
    ret = ''
    mode = 0
    for idx in range(len(code)):
        if code[idx] == '1':
            if mode == 0: 
                mode = 1
            else:
                mode = 0
        else:
            if mode == 0:
                if code[idx] != '1' and idx % 2 == 0:
                    ret += code[idx] 
                elif code[idx] == '1': 
                    mode = 1
            elif mode == 1:
                if code[idx] != '1' and idx % 2 == 1:
                    ret += code[idx]
                elif code[idx] == '1': 
                    mode = 0
    return "EMPTY" if len(ret) == 0 else ret