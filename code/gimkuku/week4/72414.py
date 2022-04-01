def stringtotime(str_time):
    h,m,s = str_time.split(":")
    h,m,s = int(h),int(m),int(s)
    return h*3600 + m*60 + s
    
def timetostring(int_answer):
    answer = ''
    if (int_answer // 3600) >= 10:
        answer += str(int_answer // 3600)
    else:
        answer += "0" + str(int_answer // 3600)
    answer += ":"
    if ((int_answer % 3600 )//60) >= 10:
        answer += str((int_answer % 3600 )//60)
    else:
        answer += "0" + str((int_answer % 3600 )//60)
    answer += ":"
    if ((int_answer % 3600)%60) >= 10:
        answer += str((int_answer % 3600)%60)
    else:
        answer += "0" + str((int_answer % 3600)%60)
    return answer
    
def solution(play_time, adv_time, logs):
    answer = ''
    time_dict = []
    end = stringtotime(play_time)
    adv = stringtotime(adv_time)

    time_dict = [0]*(end + 2)
    
    # 로그에서 split & string to int 
    for i in logs:
        stt, fin = i.split("-")
        stt = stringtotime(stt)
        fin = stringtotime(fin)
        # 누적합 
        time_dict[stt] += 1
        time_dict[fin] -= 1

    # 누적합 
    for i in range(1,end+1):
        time_dict[i] = time_dict[i] + time_dict[i-1]
        
    int_answer = 0
    # adv 사이즈로 배열의 합을 저장해 둘 리스트
    list_sum = []
    
    # 0-adv시간까지 본사람 숫자 세기
    elem = 0
    for i in range(adv):
        elem += time_dict[i]
    list_sum.append(elem)
    max_time = elem
    
    # 0-adv 까지 저장해둔 것을 기반으로 그전꺼에서 첫번째 꺼 빼고 뒤에 하나 더붙이고 반복
    for i in range(1,end - adv+1):
        elem = list_sum[i-1] - time_dict[i-1]+ time_dict[adv+i-1]
        list_sum.append(elem) 
        if elem > max_time :
            max_time = elem
            int_answer = i
            
    answer = timetostring(int_answer)
    # print(answer)
    return answer

solution("02:03:55","00:14:15",	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])