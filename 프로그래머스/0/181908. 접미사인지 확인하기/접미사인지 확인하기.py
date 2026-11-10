def solution(my_string, is_suffix):
    tail_list = []
    
    
    for i in range(0, len(my_string)):
        tail_list.append(my_string[i:])
    
    for k in tail_list:
        if is_suffix == k:
            return 1
    else:
        return 0
    