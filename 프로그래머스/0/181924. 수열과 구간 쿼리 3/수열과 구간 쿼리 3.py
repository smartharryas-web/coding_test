def solution(arr, queries):
    answer = []
    
    
    for query in queries:
        t = 0
        t = arr[query[0]]
        arr[query[0]] = arr[query[1]]
        arr[query[1]] = t

    return arr