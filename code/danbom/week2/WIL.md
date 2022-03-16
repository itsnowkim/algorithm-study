# 1. 양과 늑대
## ◻ 접근
가능한 모든 상황을 고려하는 깊이 탐색을 하되, 양이 모두 잡아먹히는 경우는 조건문으로 거르자.

## ◻ 풀이
### 📁 주어진 입력 및 예시 이해
|이름|설명|예시|
|------|---|---|
|info|각 노드에 있는 양 또는 늑대에 대한 정보가 담긴 배열, ( `0` : 양, `1` : 늑대 )|[0,0,1,1,1,0,1,0,1,0,1,1]|
|edges|2진 트리의 각 노드들의 연결 관계를 담은 2차원 배열 ( [`부모 노드 번호`, `자식 노드 번호`] 형태 )|[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],...]|

`info`를 따라 양의 수, 늑대의 수를 더해가며 늑대의 수가 양의 수보다 많거나 같아질 경우를 거를 수 있고,<br />
`edges`를 통해 특정 노드 번호에 대한 다음 노드 번호들을 알 수 있다.

### 📁 필요한 함수들
1. **입력 받은 노드 번호 다음으로 올 수 있는 노드 번호들을 구하는 함수**<br /><br />
    함수 입출력 설명
    |이름|설명|예시|
    |------|---|---|
    |node|`입력` 입력 받은 기준 노드 번호|0|
    |nextNodes|`리턴` 기준 노드 다음에 올 수 있는 노드 번호들|[1, 8]|
    ```python
    def getNextNodes(edges, node):
        nextNodes = []

        for e in edges:
            i,j = e # 예) e : [0, 1] / i : 0 / j : 1
            if node == i:
                nextNodes.append(j)

        return nextNodes
    ```
    <br />
2. **깊이 탐색 함수**<br /><br />
    함수 입출력 설명
    |이름|설명|예시|
    |------|---|---|
    |sheep, wolf|`입력` 각각 현재까지의 양의 수, 늑대의 수|0|
    |cnt|`입력` 현재 노드 번호|0|
    |path|`입력` 현재까지의 path나 다음에 갈 노드 번호 등을 담을 리스트 |[0, 1, 8, 7, 2, 9, 4]|
    |maxSheep|`리턴` 각 노드를 방문하면서 모을 수 있는 최대 양의 수|5|

    ```python
    def dfs(info, edges, sheep, wolf, cnt, path):
        if info[cnt]:
            wolf += 1
        else:
            sheep += 1
        if sheep <= wolf:
            return 0 # 양이 모두 잡아먹히는 경우는 조건문으로 거르기

        maxSheep = sheep

        for p in path:
            for n in getNextNodes(edges, p):
                if n not in path:
                    path.append(n)
                    maxSheep = max(maxSheep, dfs(info, edges, sheep, wolf, n, path))
                    path.pop()

        return maxSheep
    ```
    ```python
    # 중간 코드를 이런식으로 바꿔보면
    if sheep <= wolf:
        print("\nWARNING! 늑대가 양보다 많아져따!")
        return 0

    maxSheep = sheep
    for p in path:
        for n in getNextNodes(edges, p):
            if n not in path:
                path.append(n)
                print("현재까지의 path와 다음에 갈 노드 번호(마지막 원소) : " + str(path) + "\n양 : " + str(sheep) +", 늑대 : " + str(wolf) + " 니까 다음 노드로 가자!")
                maxSheep = max(maxSheep, dfs(info, edges, sheep, wolf, n, path))
                path.pop()
                print("못가니까 전 노드로 돌아가 다른 노드를 탐색하자\n현재까지의 path : " + str(path) + "\n")
    ```
    ```
    Output >>
    현재까지의 path와 다음에 갈 노드 번호(마지막 원소) : [0, 1]
    양 : 1, 늑대 : 0 니까 다음 노드로 가자!
    현재까지의 path와 다음에 갈 노드 번호(마지막 원소) : [0, 1, 8]
    양 : 2, 늑대 : 0 니까 다음 노드로 가자!
    현재까지의 path와 다음에 갈 노드 번호(마지막 원소) : [0, 1, 8, 2]
    양 : 2, 늑대 : 1 니까 다음 노드로 가자!

    WARNING! 늑대가 양보다 많아져따!
    못가니까 전 노드로 돌아가 다른 노드를 탐색하자
    현재까지의 path : [0, 1, 8]

    현재까지의 path와 다음에 갈 노드 번호(마지막 원소) : [0, 1, 8, 4]
    양 : 2, 늑대 : 1 니까 다음 노드로 가자!

    WARNING! 늑대가 양보다 많아져따!
    못가니까 전 노드로 돌아가 다른 노드를 탐색하자
    현재까지의 path : [0, 1, 8]

    현재까지의 path와 다음에 갈 노드 번호(마지막 원소) : [0, 1, 8, 7]
    양 : 2, 늑대 : 1 니까 다음 노드로 가자!
    현재까지의 path와 다음에 갈 노드 번호(마지막 원소) : [0, 1, 8, 7, 2]
    양 : 3, 늑대 : 1 니까 다음 노드로 가자!
    현재까지의 path와 다음에 갈 노드 번호(마지막 원소) : [0, 1, 8, 7, 2, 4]
    양 : 3, 늑대 : 2 니까 다음 노드로 가자!
    ```

3. **솔루션 함수**<br />

    ```python
    def solution(info, edges):
        sheep = 0
        wolf = 0
        cnt = 0
        path = [0] # 항상 루트 노드(0번 노드)부터 시작
        answer = dfs(info, edges, sheep, wolf, cnt, path)

        return answer
    ```

<br />

# 3. 신고 결과 받기
## ◻ 접근
한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리되니 중복을 제거해주자.

## ◻ 풀이
### 📁 주어진 입력 및 예시 이해
|이름|설명|예시|
|------|---|---|
|id_list|이용자의 ID가 담긴 문자열 배열|["muzi", "frodo", "apeach", "neo"]|
|report|각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열|["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]|
|k|이용자의 정지 기준이 되는 신고 횟수|2|

`id_list`에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 리턴하면 되므로,<br />
`answer`를 `id_list`의 길이만큼 0으로 이루어진 배열로 초기화한다.<br />
동일한 유저에 대한 신고 횟수를 1회로 처리하기 위해 `set(report)`로 중복을 제거해준다.

### 📁 솔루션 함수
|이름|설명|예시|
|------|---|---|
|answer|각 유저별로 처리 결과 메일을 받은 횟수가 담긴 배열|[2,1,1,0]|
|reported|각 유저의 id와 유저별로 신고 받은 횟수가 담긴 딕셔너리|{'muzi': 0, 'frodo': 0, 'apeach': 0, 'neo': 0}|
```python
def solution(id_list, report, k):
  answer = [0 for i in range(len(id_list))]
  reported = {x : 0 for x in id_list}

  report = set(report)

  for r in report:
      reported[r.split()[1]] += 1

  for r in report:
      if reported[r.split()[1]] >= k:
          answer[id_list.index(r.split()[0])] += 1

  return answer
```
