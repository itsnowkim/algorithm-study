dx = [1,-1,0,0]
dy = [0,0,1,-1]

def play(nowx, nowy, otherx, othery, now_player):
    
    # 지금 있는곳이 사라지면 = 현재 플레이어는 짐
    if visit[nowx][nowy] == 0:
        return (not now_player), 0
    
    # 일단 지는거로 냅둠 (좌우 양옆 이동했는데도 지고 있으면 진거)
    state = False
    step = 0

    for i in range(4):
        # 다음으로 갈곳
        nx = nowx + dx[i]
        ny = nowy + dy[i]
        
        # 보드 밖으로 가면 멈춤
        if nx >= w or ny >= h or nx < 0 or ny < 0 : 
            continue
        # 이미 갔던 곳이면 멈춤
        if visit[nx][ny] == 0 :
            continue

        visit[nowx][nowy] = 0
        # 상대랑 나랑 턴이 바뀜 -> 게임 다시 진행
        if now_player:
            pre_winner, pre_step = play(otherx, othery, nx, ny, False)
        else:
            pre_winner, pre_step = play(otherx, othery, nx, ny, True)
        
        # 칸수 + 1 
        pre_step = pre_step + 1
        
        # 백트래킹
        visit[nowx][nowy] = 1
        
        # 지금 차례인 사람이 지고 있는데 (=state)
        # 이 전 상태가 이기는 방법일 경우 :
        if not state and (pre_winner == now_player):
            step = pre_step
            state = True
        # 이 전 상태도 지는 방법일 경우 -> 오래 버티는 방법
        elif not state and (pre_winner != now_player): 
            step = max(pre_step, step)
        # 지금 차례인 사람이 이기고 있으면, 이전도 이길때만 업뎃 & 걍 빨리 이기기! 
        elif state and (pre_winner == now_player): 
            step = min(pre_step, step)
    
    if now_player == state:
        winner = True
    else:
        winner = False
    return winner, step


def solution(board_list, aloc, bloc):
    
    global w,h,visit
    w, h = len(board_list), len(board_list[0])
    # 방문 여부 체크용
    visit = board_list
    winner, answer = play(aloc[0], aloc[1], bloc[0], bloc[1],True)
    return answer

# solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]],	[1, 0],	[1, 2])