def solution(num_list):
    a = 1
    b = 0
    
    for i in num_list:
        a *= i
    
    for k in num_list:
        b += k
        
    if a < (b**2):
        return 1
    else:
        return 0