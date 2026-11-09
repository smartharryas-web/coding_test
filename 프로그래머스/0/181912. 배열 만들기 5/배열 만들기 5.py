def solution(intStrs, k, s, l):
    answer = []
    
    for intStr in intStrs:
        a = intStr[s:s+l]
        if int(a) > k:
            answer.append(int(a))

    return answer