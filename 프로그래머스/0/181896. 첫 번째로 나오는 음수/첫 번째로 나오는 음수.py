def solution(num_list):
    answer = 0
    k = 0
    
    for i in num_list:
        if i < 0:
            return k 
        k += 1
    else:
        return -1
