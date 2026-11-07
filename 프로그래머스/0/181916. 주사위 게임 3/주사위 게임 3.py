def solution(a, b, c, d):
    dice = [a, b, c, d]
    
    # 1. 네 주사위의 숫자가 모두 같은 경우
    if len(set(dice)) == 1:
        return 1111 * a
    
    # 2. 네 주사위의 숫자가 모두 다른 경우
    elif len(set(dice)) == 4:
        return min(dice)
    
    # 3. 어느 두 주사위만 같고 나머지 두 주사위는 다른 경우 (집합 크기 = 3)
    elif len(set(dice)) == 3:
        q_and_r = []
        for x in set(dice):
            if dice.count(x) == 1:
                q_and_r.append(x)
        return q_and_r[0] * q_and_r[1]
    
    # 4. 세 주사위가 같거나, 두 개씩 같은 경우 (집합 크기 = 2)
    else:
        for x in set(dice):
            # 세 주사위가 같은 경우 (3개 / 1개)
            if dice.count(x) == 3:
                p = x
                q = 0
                for y in set(dice):
                    if y != p:
                        q = y
                        break
                return (10 * p + q) ** 2
        
        # 두 개씩 같은 경우 (2개 / 2개)
        p, q = list(set(dice))
        return (p + q) * abs(p - q)