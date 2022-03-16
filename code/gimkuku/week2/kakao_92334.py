def solution(id_list, report, k):
    report_num = [0]*len(id_list) # 신고 당한 횟수
    answer = [0]*len(id_list) # 메일 횟수
    reported_list = [] # 신고당한 인간
    
    # report 중복 제거
    report_set = set(report[:])
    for i in list(report_set):
        reporter, reported = i.split(' ')
        idx = id_list.index(reported)
        report_num[idx] += 1
    print(report_num)

    # 신고당한 인간 찾기
    for idx, i in enumerate(report_num):
        if i >= k:
            reported_list.append(id_list[idx])
    print(reported_list)

    # 메일 보내기
    for i in report:
        reporter, reported = i.split(' ')
        if reported in reported_list:
            idx = id_list.index(reporter)
            answer[idx] +=1
    
    print(answer)
    return answer


solution(["muzi", "frodo", "apeach", "neo"],	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)