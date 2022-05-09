def solution(record):
    answer = []
    # record를 배열에 넣기.
    # uid로 닉넴 구별, hash
    # history[]에 닉넴 출력 ㄴㄴ, uid로 각 유저 행동 저장
    # 최종 답에서 uid를 닉넴으로 교체해서 리턴
    
    history = []
    
    user = {}
    
    for rec in record:
        command = rec.split()
        if len(command) == 2:
            # leave
            history.append([command[1],'님이 나갔습니다.'])
        else:
            try:
                temp_name = user[command[1]]
                if temp_name != command[2]:
                    user[command[1]] = command[2]
            except KeyError:
                user[command[1]] = command[2]
            
            # command에 따른 history 저장
            if command[0] == 'Enter':
                history.append([command[1],'님이 들어왔습니다.'])
            
    for record in history:
        answer.append(user[record[0]] + record[1])
        
    
    return answer