def calc(apeach,lion):
    apeach_sum = 0
    lion_sum = 0
    
    for i in range(11):
        if ((apeach[i] == lion[i]) and (apeach[i] == 0)):
            continue
        if (apeach[i] < lion[i]):
            lion_sum = lion_sum + 10 - i
        else:
            apeach_sum = apeach_sum + 10 - i

    if (lion_sum > apeach_sum):
        return lion_sum - apeach_sum
    else:
        return -1

# 초기 k = 11

def make_lion_list(info, temp_list, n,k):
    calc_result = 0
    sub_temp_list = temp_list[:]
    answer_list = sub_temp_list
    
    if k == 1:
        sub_temp_list.append(n)
        calc_result = calc(info, sub_temp_list)
        return calc_result, sub_temp_list
    
    max_num = -1
    for i in range(n+1):
        sub_temp_list.append(i)
        calc_result, list_result = make_lion_list(info,sub_temp_list,n-i,k-1)
        if calc_result == -1:
            sub_temp_list = temp_list[:]
            continue
        # 더 클때는 max값 비교               
        if (max_num < calc_result):
            max_num = calc_result
            answer_list = list_result[:]
        # 같을때는 더 아래있는 숫자 비교
        elif(max_num == calc_result):
            for j in range(11):
                if (answer_list[10-j] == list_result[10-j] ): 
                    continue
                else:
                    if (answer_list[10-j] > list_result[10-j] ): 
                        break
                    else: 
                        answer_list = list_result[:]
                        break
            
        sub_temp_list = temp_list[:]
        
    if max_num == -1:
        answer_list = [-1]
        
    return max_num, answer_list
    
def solution(n, info):
    answer = []
    answer_list = []
    k, answer = make_lion_list(info, answer_list, n, 11)
    
    return answer