def nextnode(now,edges):
    queue = []
    for i in edges:
        if i[0] == now:
            queue.append(i[1])
        if i[1] == now:
            queue.append(i[0])
    return queue
    
def dfs(now, sheep, wolf, info, edges, cango_list, new_visit_list):
    global max_sheep
    new_visit = new_visit_list[:]
    cango = cango_list[:]

    # 첫 방문 노드라면 0로 바꿔주고 늑대 & 양 개수 업데이트
    if new_visit[now]:
        new_visit[now] = 0
        if info[now] == 0 : sheep = sheep + 1 
        else : wolf = wolf + 1
    
        # 현재 양이 max인지 체크
        if (sheep > max_sheep) :
            max_sheep = sheep
            
    # 다 잡아먹히면 return
    if (sheep == wolf) : 
        return 0
    
    # 아니면 계속 진행해보기
    cango = cango + nextnode(now,edges)
    for i in cango:
        # 방문을 안했었던 노드 방문
        if new_visit[i]:
            max_sheep = max(max_sheep, dfs(i, sheep, wolf, info, edges, cango, new_visit))

    return max_sheep
    

def solution(info_list, edges):
    global max_sheep, info
    info = info_list
    max_sheep = 0
    new_visit = [1]*(len(info))
    cango = []
    
    dfs(0,0,0,info,edges,cango, new_visit)
    
    return max_sheep