def solution(rank, attendance):
    
    # rank : [3, 7, 2, 5, 4, 6, 1]
    # attendance : [f, t, t, t, t, f, f]
    # result : 20403
    
    a_b_c = []
    value = 1
    
    while len(a_b_c) != 3:
        # rank의 제일 작은 수 인덱스 찾기 찾기
        # if attendance == true:
        #   a_b_c.append
        if attendance[rank.index(value)]:
            a_b_c.append(rank.index(value))
        value += 1
            
    return 10000 * a_b_c[0] + 100 * a_b_c[1] + a_b_c[2]