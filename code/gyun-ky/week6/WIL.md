# WIL

## 괄호 변환 (60058)
문제에서 요구하는 것만 잘 구현하면 풀수 있는 문제였습니다.
오랜만에 recursion 파티를 하려니까 잠깐 헷갈렸지만 금방 감 잡았습니다.
늘 recursion break 조건과 예외처리에 촉각을 곤두세워야 할거 같습니다~~

코드에 한줄한줄 주석 달며 과정을 써놨습니당


## 블록 이동하기 (60063)
처음에 생각한대로 풀다보니 이것저것 꼬여서 굉장히 더러운 코드가 되어버렸습니다...!

- 전체적인 방법 : visited를 두개 선언하여 BFS -> 해당 배열은 삼차원으로 선언했습니다.
    - 하나는 로봇이 가로로 있는 경우 visited[0][a][b]
    - 하나는 로봇이 세로로 있는 경우 visited[1][a][b]

### 각 함수 설명

- check_boundary
    - Return True / False
    - 이동한 위치가 지도 안에 있는지 경계 확인 

- change_rot
    - Return 'h' - 가로 / 'v' - 세로
    - 회전을 하게되면 무조건 방향이 바뀌는데 이 부분을 구현한 메서드

- check_visited
    - Return True / False
    - 이동한 위치가 이전에 방문하지 않았는지 확인
    - 가로(h)이면 visited[0][a][b] 확인 
    - 세로(v)이면 visited[1][a][b] 확인
    - 만약 방문 가능한 곳이면 -> visited True 처리 후 True 반환 (방문처리 통상적인 BFS랑 달리 메서드 안에 넣어서 혼란을 드려 죄송.. bad code..)

- rotation_v(a, b, c, d)
    - 현재 로봇이 세로로 놓여있는 경우 rotation
    - return (회전가능한지(Boolean), 좌표1x, 좌표1y, 좌표2x, 좌표2y)
    1. 회전시 방향이 바뀔 것이기 때문에 change_rot 호출
    2. 해당 메서드는 a,b가 위칸인 경우를 가정하고 만들어졌으므로, a,b가 아래에 있다면 c,d와 swap  --> 이 부분때문에 오래 걸렸습니다.....
    3. 각각의 rotation 실행 
        - rotation 가능하면 (True, 바뀐 좌표) return
        - rotation 불가하면 (False, 원래 좌표) return

- rotation_h(a, b, c, d)
    - 현재 로봇이 가로로 놓여있는 경우 rotation
    - 상위 rotation_v와 로직 동일합니다!!

- bfs
    - 일반적임 BFS!
    - rotation, 상하좌우 움직이기!

결론적으로 굉장히 더러운 코드가 되었습니다. 그래서 일단 타 블로그 보고 좀 정리하고자 합니다!!! 제출 전까지 함 코드 개선이 될지는 모르겠습니다. 개선된 코드는 60063-2.py로 올립니다

