def solution(my_string, index_list):
    answer = ''
    
    for k in index_list:
        answer += my_string[k]
    
    
    return answer