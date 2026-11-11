def solution(my_string, is_prefix):
    answer = []
    
    for i in range(0, len(my_string)):
        answer.append(my_string[0:i])
    
    
    for k in answer:
        if k == is_prefix:
            return 1
    else:
        return 0           
