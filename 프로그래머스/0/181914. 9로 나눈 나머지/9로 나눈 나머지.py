def solution(number):
    answer = 0
    k = 0
    
    for i in number:
        k += int(i)
    
    return k % 9