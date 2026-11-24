def solution(arr):
    answer = []
    m = 0
    n = 0
    n_array = []
    
    
    for i in arr:
        if i == 2:
            m += 1
    
    if m == 0:
        answer.append(-1)
    
    if m == 1:
        answer.append(2)
    
    if m >= 2:
        for k in arr:
            if k == 2:
                n_array.append(n)
            n += 1
        return arr[n_array[0]:n_array[-1]+1]
    
    return answer