def solution(id_list, report, k):
    
    report_info = {}
    reported_count = {}
    
    fired = []
    answer = []
    
    
    # 딕셔너리 만들기 (신고 내역)
    for i in id_list:
        report_info[i] = set()
        reported_count[i] = 0
    # 딕셔너리 값 만들기
    for r in report:
        temp = r.split()
        #중복 제거 되어야 함 / 셋 선언으로 됨
        report_info[temp[0]].add(temp[1])
    
    for s in report_info:
        for target in report_info[s]:
            reported_count[target] += 1
    
    for user in reported_count:
        if reported_count[user] >= k:
            fired.append(user)
    
    for user in id_list:
        mail_count = 0
        for target in report_info[user]:
            if target in fired:
                mail_count += 1
        answer.append(mail_count)
    
    return answer