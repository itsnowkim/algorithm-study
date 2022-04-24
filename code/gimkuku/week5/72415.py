from collections import deque

def solution(board, r, c):
    # answer = 0
    # 한줄로 붙여버리기
    board = ''.join(str(each) for row in board for each in row)
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    # y, x, count, enter, board 
    # enter = -1 : 아직 아무것도 안까진 상태
    # enter != -1 : 그 자리에 있는 애가 현재 까져있음
    que = deque([(r, c, 0, -1, board)])
    visited = set()
    
    # queue 가 남아 있을 때
    while que:
        # y,x : 현위치, count : 이동 횟수, enter
        # 큐에서 하나씩 빼기
        y, x, count, enter, board = que.popleft()
        # 전체 방문 시 count 리턴
        if board.count('0') == 16 : 
            return count
        # 방문해본곳이면 pass
        if (y, x, enter, board) in visited:
            continue
        # 아니라면 방문한거에 넣기
        visited.add((y, x, enter, board))
        
        # 이동시작
        for dy, dx in directions:
            # 그냥 앞뒤양옆 -> 큐에 넣기
            ny, nx = y + dy, x + dx
            if 0 <= ny < 4 and 0 <= nx < 4:
                que.append ((ny, nx, count + 1, enter, board))
                
            # 컨트롤 앞뒤양옆
            ny,nx = ctrl_move(y, x, dy, dx, board)
            # 제자리면 패스
            if ny == y and nx == x:
                continue
            que.append((ny, nx, count + 1, enter, board))
            
        position = y * 4 + x
    
        # 아직 안없어진 애면
        if board[position] != 0:
            # 처음 만나는 앤데 아직 까져있는게 없으면 얘를 까자
            if enter == -1:
                que.append((y, x, count + 1, position, board))
            # 하나 까져있고, 얘는 까진 애가 아니고, 근데 같으면
            elif enter != position and board[enter]== board[position]:
                # 둘다 0으로 바꾸기
                board =board.replace(board[enter], '0')
                # 다시 안까진 상태(enter = -1)로 바꾸고, enter 눌렀으니까 count++
                que.append((y, x, count + 1, -1, board))
            # 아무것도 아니면 쿨하게 패스
    return count

def ctrl_move(y, x, dy, dx, board):
    ny, nx = y + dy, x + dx
    if 0 <= ny < 4 and 0 <= nx < 4:
        # 빈곳이면 누군가 만날때까지 보내기
        if board[ny * 4 + nx] == '0':
            return ctrl_move(ny, nx, dy, dx, board)
        else:
            return ny, nx
    # 자리없으면 안보내기 (= 맨끝까지 보내기)
    else:
        return y, x


