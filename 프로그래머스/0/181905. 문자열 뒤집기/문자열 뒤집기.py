def solution(my_string, s, e):
    
    temp1 = []
    temp2 = []
    answer = ''
    
    for i in my_string[s:e+1]:
        temp1.append(i)
    
    for k in my_string:
        temp2.append(k)
    
    temp2[s:e+1] = temp1[::-1]
    
    answer = ''.join(temp2)

    return answer