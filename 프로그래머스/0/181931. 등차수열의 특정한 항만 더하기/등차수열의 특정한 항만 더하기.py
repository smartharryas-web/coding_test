def solution(a, d, included):
    answer = 0
    k = 0
    
    
    for i in included:
        if i:
            answer += a + k*d
        k += 1
        
    return answer