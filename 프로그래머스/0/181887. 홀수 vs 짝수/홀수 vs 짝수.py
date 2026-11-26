def solution(num_list):
    
    odd = 0
    even = 0
    
    for i in num_list[::2]:
        odd += i
    
    for k in num_list[1::2]:
        even += k
        
    if even >= odd:
        return even
    else:
        return odd