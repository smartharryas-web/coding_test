def solution(code):
    idx = 0
    mode = 0
    ret =''
    
    for co in code:
        if mode == 0:
            if co != '1':
                if idx % 2 == 0:
                    ret += co
            else:
                mode = 1
        else:
            if co != '1':
                if idx % 2 == 1:
                    ret += co
            else:
                mode = 0
        idx += 1
            
    if ret == '':
        return "EMPTY"
    else:
        return ret