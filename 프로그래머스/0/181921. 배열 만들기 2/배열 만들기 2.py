def solution(l, r):
    
    a = []
    b = ''
    
    for i in range(l, r+1):
        b = ''
        for k in str(i):
            if k in ('1', '2', '3', '4', '6', '7', '8', '9'):
                break
            else:
                b += k
        else:
            a.append(int(b))
    
    if a == []:
        a.append(-1)

    return a