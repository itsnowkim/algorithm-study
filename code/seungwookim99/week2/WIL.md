# WIL : Week 2
2주차에 대한 WIL

# kakao_92334 : 신고 결과 받기
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/92334
## Solved Code
```python
def solution(id_list, report, k):
    answer = []
    report_dict = {}
    
    # 신고 정보 딕셔너리 초기화
    for i in id_list:
        tmp = dict()
        tmp['count'] = 0  # 누적 신고 횟수
        tmp['report_from'] = [] # 나를 신고한 사람
        tmp['report_to'] = [] # 내가 신고한 사람
        report_dict[i] = tmp
        
    for rep in report:
        r_from, r_to = rep.split(' ')
        # 처음 신고한다면
        if r_to not in report_dict[r_from]['report_to']:
            report_dict[r_from]['report_to'].append(r_to)
            report_dict[r_to]['report_from'].append(r_from)
            report_dict[r_to]['count'] += 1
    
    # 정지당한 계정 추출
    blocked_list = []
    for i, info in report_dict.items():
        if info['count'] >= k:
            blocked_list.append(i)
    
    # 집합으로 만듬
    blocked_set = set(blocked_list)
    
    # 발송할 메일 횟수 계산
    for _, info in report_dict.items():
        report_to = set(info['report_to'])
        answer.append(len(report_to&blocked_set)) # 교집합 원소 개수
    return answer
```
### 결과
성공
### 접근
- 신고 정보를 다음과 같이 report_dict에 저장한다. (id list 순서대로 저장)
```python
{
  "muzi" : {
    "count" : 0, # 내가 신고당한 누적 횟수
    "report_from" : [], # 나를 신고한 id 리스트
    "report_to" : [], # 내가 신고한 id 리스트
  },
  ...
}
```
- report 문자열 리스트 정보를 읽어와 `report_from`, `report_to`로 split 한다
- `if r_to not in report_dict[r_from]['report_to']`로 `report_from`이 `report_to`를 처음 신고하는 경우에만 정보를 갱신한다
- 갱신할 정보는 신고당한 횟수와 누가 누구를 신고했는지 양방향으로 담는다
- 정지당한 계정 리스트를 추출하여 set으로 만든다
- report_dict를 순회하며 내가 신고한 id들이 담긴 `report_to`를 추출해 set으로 만든다
- 위에서 만든 두 set을 교집합 연산하여 개수를 answer에 append 한다

## 92334 : 신고 결과 받기 문제 회고
처음 주어진 id_list 순서대로 답을 구해야 하기 때문에, 처음부터 id_list대로 정보를 저장했다.
내가 신고한 유저 집합과 정지당한 유저 집합의 교집합 연산을 통해 발송할 메일 개수를 구했다.
조건대로 구현하기만 하면 되는 비교적 간단한 문제였던 것 같다.

# kakao_92344 : 파괴되지 않은 건물
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/92344
## Solved Code
```python
def solution(board, skill):
    answer = 0
    height, width = len(board), len(board[0])
    matrix = [[0] * (width+1) for _ in range(height+1)] # (height+1) x (width+1) matrix

    # 시작 좌표, 끝 좌표 기록 : O(len(skill))
    for type, r1, c1, r2, c2, degree in skill:
        degree *= (-1) if type == 1 else 1
        matrix[r1][c1] += degree
        matrix[r2+1][c2+1] += degree
        matrix[r1][c2+1] -= degree
        matrix[r2+1][c1] -= degree
        
    # 누적 합 계산 : O(width*height)
    # 가로 방향 (좌->우) 누적합 계산
    for i in range(1,width+1):
        for j in range(height+1):
            matrix[j][i] += matrix[j][i-1]
    
    # 세로 방향 (상->하) 누적합 계산
    for j in range(1,height+1):
        for i in range(width+1):
            matrix[j][i] += matrix[j-1][i]
    
    # 파괴되지 않은 건물 개수 계산
    for y in range(height):
        for x in range(width):
            if board[y][x] + matrix[y][x] > 0 :
                answer += 1
    return answer
```
### 결과
성공
### 접근
누적합 문제를 빠른 시간복잡도에 풀 수 있는 `imos` 알고리즘으로 해결했다
## 92344 : 파괴되지 않은 건물 문제 회고
도저히 나 스스로는 해결하기 어려웠던 문제,,, 문제 해결까지의 과정을 회고해보겠다.

대부분 문제를 읽고 바로 naive한 해결법이 떠올랐을 것이다. 그런데 첫 줄에 `[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]` 라는 문구를 보고
naive하게 접근하면 안된다는 걸 알았다. 그래도 궁금해서 바로 떠오른 해결법대로 구현을 해봤다.

skill을 순회하며 좌표값들을 받아 board를 좌표의 영역만큼 매 번 순회하며 더하거나 빼는 식으로 구현했다. 결과는 `정확성 100점 효율성 0점으로 실패`.
그도 그럴 것이 시간복잡도가 `O(N*M*skill길이)`, 대략 25만x1000x1000이기 때문이다.

두 가지로 접근하며 생각해봤다.

1. skill을 순회하며 매 번 좌표에 값을 더하는 과정을 O(1)로 구현하자. 그럼 최종 시간복잡도는 O(skill길이) 일 것.
2. skill을 순회하며 좌표값들을 저장한 후, 마지막에 board 전체를 순회하며 한 번에 더하자. 그럼 최종 시간복잡도는 O(skill길이 + N*M) 일 것.

처음에는 첫번째 접근에만 매달렸다. 우리는 시각적으로 행렬 위에 직사각형 면적 단위로 덧셈을 할 수 있지만 컴퓨터는 기본적으로 하나하나 순회를 해야 한다. 이 과정에서 순회를 빼고 면적 단위로 O(1)에 덧셈을 할 방법이 있을거라 생각했다. 그런데 도저히 방법이 떠오르지 않았다.

두번째 접근은 가능한 방법인가 싶어서 의문이 들었는데 옆에서 같이 공부하던 현재형이 문제에 대해 검색해보고 `imos`알고리즘을 활용하면 가능하다고 힌트를 줬다. `imos` 알고리즘을 검색해보자마자 해결법이 떠올랐고 바로 구현해서 문제 해결에 성공했다. 알고리즘 설명글은 아래 레퍼런스에 남겨뒀다.

돌이켜보면 imos 알고리즘의 기본 컨셉은 혼자 생각하기 어려웠을 것 같다. 그런데 1차원에서 적용하는 개념을 2차원으로 확장하는 컨셉은 조금 더 고민해본다면 떠올렸을수도 있겠다 싶었다. 알고리즘 수업 때 1차원 배열 상에서 Maximum Subsequence Sum을 구하는 로직을 2차원으로 확장시키는 방법을 배웠는데 컨셉이 유사했다. 2차원 matrix를 1차원으로 정사영시켜 해결했던 방법이다. 주어진 문제의 해결 과정에서도 2차원 matrix를 1차원 방향으로 누적합을 구하며 정사영 시키는 느낌이 들었다.

### Ref
[imos 알고리즘 소개](https://driip.me/65d9b58c-bf02-44bf-8fba-54d394ed21e0)