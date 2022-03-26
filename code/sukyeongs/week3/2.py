def solution(rows, columns, queries):
    answer = []

    graph = [list(range(1 + (i * columns), 1 + (i * columns) + columns)) for i in range(rows)]

    for query in queries:
        x1, y1, x2, y2 = query
        temp1 = graph[x1 - 1][y2 - 1]
        temp2 = graph[x2 - 1][y2 - 1]
        temp3 = graph[x2 - 1][y1 - 1]        
        ans = min(temp1, temp2, temp3)
        for i in range(y2 - 1, y1 - 1, -1):
            graph[x1 - 1][i] = graph[x1 - 1][i - 1]
            ans = min(ans, graph[x1 - 1][i])

        for i in range(x2 - 1, x1, - 1):
            graph[i][y2 - 1] = graph[i - 1][y2 - 1]
            ans = min(ans, graph[i][y2 - 1])

        for i in range(y1 - 1, y2 - 1):
            graph[x2 - 1][i] = graph[x2 - 1][i + 1]
            ans = min(ans, graph[x2 - 1][i])

        for i in range(x1 - 1 , x2 - 2):
            graph[i][y1 - 1] = graph[i + 1][y1 - 1]
            ans = min(ans, graph[i][y1 - 1])
            
        graph[x1][y2 - 1] = temp1
        graph[x2 - 1][y2 - 2] = temp2
        graph[x2 - 2][y1 - 1] = temp3
        answer.append(ans)

    return answer
