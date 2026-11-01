def solution(a, b):
    
    c, d = str(a), str(b)
    if int(c+d) >= int(d+c):
        return int(c+d)
    else:
        return int(d+c)