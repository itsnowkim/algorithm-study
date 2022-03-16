def solution1(board, skill):
    answer = 0
    board_list = board[:]
    for x in range(len(board_list)):
        for y in range(len(board_list[0])):
            print("x, y : ",x,y)
            for i in skill:
                r1,c1,r2,c2,degree = i[1],i[2],i[3],i[4],i[5]
                if (x >= r1 and x<= r2)and(y>=c1 and y<=c2):
                    # 공격스킬
                    if i[0] == 1:
                        board_list[x][y] += degree
                        print("get  ",x,y)          
                    # 방어스킬
                    else:
                        board_list[x][y] -= degree       
            if board_list[x][y] > 0:
                answer += 1
    print(answer)
    return answer

# 이게 정답코드 
def solution2(board, skill):
    answer = 0
    board_list = board[:]
    # 누적합 배열
    multisum_list = [[0]*(len(board_list[0])+1) for i in range(len(board_list)+1)]
    
    for i in skill:
        r1,c1,r2,c2,degree = i[1],i[2],i[3],i[4],i[5]
        # 공격스킬
        if i[0] == 1:
            multisum_list[r1][c1] -= degree 
            multisum_list[r1][c2+1] += degree    
            multisum_list[r2+1][c1] += degree    
            multisum_list[r2+1][c2+1] -= degree    
        # 방어스킬
        else:
            multisum_list[r1][c1] += degree 
            multisum_list[r1][c2+1] -= degree    
            multisum_list[r2+1][c1] -= degree    
            multisum_list[r2+1][c2+1] += degree   

    # 누적합 가로 진행
    for i in range(len(board)):
        for j in range(1,len(board[0])):
            multisum_list[i][j] += multisum_list[i][j-1]
    
    # 누적합 세로 진행
    for i in range(len(board[0])):
        for j in range(1,len(board)):
            multisum_list[j][i] += multisum_list[j-1][i]
            
    for x in range(len(board)):
        for y in range(len(board[0])): 
            if board_list[x][y] > (multisum_list[x][y]* -1):
                answer += 1
    
    return answer