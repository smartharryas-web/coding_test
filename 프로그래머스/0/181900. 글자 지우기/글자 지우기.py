def solution(my_string, indices):
    answer = ''
    temp = []
    t = 0
    
    indices.sort()
    
    for i in my_string:
        temp.append(i)
    
    for k in indices:
        del temp[k-t]
        
        t += 1
    
    
    answer = ''.join(temp)
    
    return answer