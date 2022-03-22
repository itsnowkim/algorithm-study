def circle(x1,x2,y1,y2):
    min_num = board[x1][x2]
    temp1, temp2, temp3 = 0, 0, 0

    temp1 = board[x1][x2]
    for i in range(x1, y1):
        if board[i+1][x2] < min_num:
            min_num = board[i+1][x2]
        board[i][x2] = board[i+1][x2] 

    temp2 = board[x1][y2]
    for i in range(y2-1, x2-1, -1):
        if board[x1][i] < min_num:
            min_num = board[x1][i]
        board[x1][i+1] = board[x1][i]
    board[x1][x2 + 1] = temp1

    temp3 = board[y1][y2]
    for i in range(y1-1, x1-1, -1):
        if board[i][y2] < min_num:
            min_num = board[i][y2]
        board[i+1][y2] = board[i][y2]
    board[x1+1][y2] = temp2
        
    for i in range(x2, y2):
        if board[y1][i] < min_num:
            min_num = board[y1][i]
        board[y1][i] = board[y1][i+1]
    board[y1][y2 - 1] = temp3
    
    if min(temp1,temp2,temp3) < min_num:
        min_num = min(temp1,temp2,temp3)
    return min_num
    
def solution(rows, columns, queries):
    answer = []
    
    global board
    index = 1
    board = []
    
    for i in range(rows):
        element = []
        for j in range(columns):
            element.append(index)
            index = index +1
        board.append(element)

    for i in queries:
        x1,x2,y1,y2 = i[0],i[1],i[2],i[3]
        answer.append(circle(x1-1,x2-1,y1-1,y2-1))
        
    return answer