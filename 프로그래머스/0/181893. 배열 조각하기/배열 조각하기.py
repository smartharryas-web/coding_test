def solution(arr, querys):
    query_index = 0
    
    for query in querys:
        if query_index % 2 == 0:
            del arr[query+1:]
        elif query_index % 2 == 1:
            del arr[:query]
        query_index += 1
    
    return arr