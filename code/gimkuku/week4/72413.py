maxnum = 200000001
def solution(n, s, a, b, fares):
    s,a,b = s-1,a-1,b-1 
    
    # 거리 리스트 초기화
    dist = []
    for i in range(n) : 
        dist.append([maxnum]*n)
    for i in range(n) : 
        dist[i][i] = 0
    for p1,p2,d in fares:
        dist[p1-1][p2-1] = d
        dist[p2-1][p1-1] = d
    
    # 최소 거리로 업뎃
    # nextnode, i , j 순서로 하면 되고
    # i,nextnode, j 순서로 하면 틀림
    # 왜지?ㅋㅋ
    for nextnode in range(n):
        for i in range(n):
            for j in range(n):
                if i==j : continue
                if dist[i][nextnode] != maxnum and dist[nextnode][j] != maxnum:
                        dist[i][j] = min(dist[i][j], dist[i][nextnode] + dist[nextnode][j])
                        dist[j][i] = dist[i][j] 

    # 최소값 찾기
    answer = maxnum
    for h in range(n):
        answer = min(answer, dist[s][h] + dist[h][a] + dist[h][b])

    return answer


# solution(6,	4,	6,	2,	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])