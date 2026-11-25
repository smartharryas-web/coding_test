def solution(str_list):
    index = 0
    
    for i in str_list:
        if i == 'l':
            return str_list[:index]
        elif i == 'r':
            return str_list[index+1:]
        index += 1
        
        
    return []