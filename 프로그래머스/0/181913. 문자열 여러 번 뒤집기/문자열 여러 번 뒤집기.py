def solution(my_string, queries):
    answer = ''
    
    for query in queries:
        s = query[0]
        e = query[1]
        
        temp = []
        temp_2 = []
        t = 0
        
        for i in my_string[s:e+1]:
            temp.append(i)
        
        for m in my_string:
            temp_2.append(m)
            
        for k in temp[::-1]:
            temp_2[s + t] = k
            t += 1
        my_string = ''.join(temp_2)
    
    return my_string