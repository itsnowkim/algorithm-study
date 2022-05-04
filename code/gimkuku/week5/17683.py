def strtotime(start,end):
    st_hh,st_mm = start.split(":")
    e_hh,e_mm = end.split(":")
    return ((int(e_hh) - int(st_hh)) * 60 + (int(e_mm) - int(st_mm)))
    
def solution(m, musicinfos):
    answer = ''
    m_list = []
    info_dict = {}
    # m과 musicinfos를 아스키코드 숫자 배열로 바꿈
    # 이때 #은 아스키코드 + 7
    for i in m:
        if i != '#':
            m_list.append(ord(i))
        else:
            m_list[-1] += 7
    # m을 string으로 만들기
    m_str = ""
    for i in m_list:
        m_str += str(i)
    
    for i in musicinfos:
        start,end,title,info = i.split(',')
        element = []
        playtime = strtotime(start,end)
        print(playtime)
        idx = 0 
        while(idx < playtime ):
            j = info[idx % len(info)]
            if j != '#':
                element.append(ord(j))
            else:
                element[-1] += 7
                playtime += 1
            idx += 1
        if info[idx % len(info)] == "#":
             element[-1] += 7
        # element를 string으로 만들기 -> info_dict에 넣기
        info_str = ""
        for j in element:
            info_str += str(j)
        info_dict[title] = info_str
    print(m_str)
    print(info_dict)
    len_answer = 0
    for i in info_dict:
        if m_str in info_dict[i]:
            if(len_answer < len(info_dict[i])):
                len_answer = len(info_dict[i])
                answer = i
    if answer == '': return "(None)"
    return answer
    
# solution("ABCDEFG",	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
# solution("CC#BCC#BCC#BCC#B", ["03:50,04:00,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])
solution("ABC", ["12:00,12:14,HELLO,DEFGABC#", "13:00,13:05,WORLD,ABCDEF"])