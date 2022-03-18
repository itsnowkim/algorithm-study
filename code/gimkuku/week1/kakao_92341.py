import math

def calc_time(in_time,out_time):
    in_time_list = in_time.split(":")
    out_time_list = out_time.split(":")
    in_time_to_min = int(in_time_list[0]) * 60 + int(in_time_list[1])
    out_time_to_min = int(out_time_list[0]) * 60 + int(out_time_list[1])
    return out_time_to_min - in_time_to_min 


def calc_fee(time, fees):
    if time > fees[0]:
        # 소숫점 올림으로 계산 : math.ceil
        return fees[1] + ((math.ceil((time - fees[0]) / float(fees[2]))) * fees[3])
    else:
        return fees[1]
    
    
def solution(fees, records):
    answer = []
    time_list = []
    time_dict = {}
    for i in records:
        i_list = i.split(" ")
        if i_list[2] == "IN":
            element = []
            element.append(i_list[1])
            element.append(i_list[0])
            element.append("23:59")
            time_list.append(element)
        else :
            for j in time_list:
                if j[0] == i_list[1]:
                    time = calc_time(j[1],i_list[0])
                    time_list.remove(j)
                    if time_dict.get(j[0]) == None:  
                        time_dict[j[0]] = time
                    else:
                        value = time_dict[j[0]]
                        time_dict[j[0]] = value + time
                else: continue
                
    for i in time_list:
        time = calc_time(i[1],i[2])
        if time_dict.get(i[0]) == None:  
            time_dict[i[0]] = time
        else:
            value = time_dict[i[0]]
            time_dict[i[0]] = value + time

    time_dict = sorted(time_dict.items())
    
    for i in time_dict:
        answer.append(calc_fee(i[1],fees))
        
    return answer