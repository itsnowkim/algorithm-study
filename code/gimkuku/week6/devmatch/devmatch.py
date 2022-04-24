def dfs(now, visits):
    visited = visits[:]
    visited.append(now)
    global start, dest,_max
    if (len(visited) > _max + 1):
        return
    if (now == dest):
        possible.append(visited)
        print("possible",possible)
        return 
    for i in edg:
        if i[0] == now and i[1] not in visited:
            dfs(i[1], visited)
            print("possible",possible)
        elif i[1] == now and i[0] not in visited:
            dfs(i[0], visited)
            print("possible",possible)
    print("possible",possible)

def solution(n, edges, k, a, b):
    answer = 0

    global start, dest, _max, edg,possible
    possible = []
    start, dest,_max,edg = a,b,k,edges
    dfs(start, [])
    print("main",possible)
    for i in possible:
        for j in range(len(i) - 1):
            print([i[j],i[j+1]])
            if [i[j],i[j+1]] in edges:
                answer = answer + 1
                edges.remove([i[j], i[j + 1]])
            if [i[j+1],i[j]] in edges:
                answer = answer + 1
                edges.remove([i[j+1],i[j]])

    print(answer)
    return answer
    
    
    return answer



solution(8,	[[0,1],[1,2],[2,3],[4,0],[5,1],[6,1],[7,2],[7,3],[4,5],[5,6],[6,7]],	4,	0,	3)