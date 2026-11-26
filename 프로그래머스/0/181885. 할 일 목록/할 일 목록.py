def solution(todo_list, finished):
    
    answer = []
    index = 0
    
    for i in finished:
        if i == False:
            answer.append(todo_list[index])
        index += 1
    
    return answer