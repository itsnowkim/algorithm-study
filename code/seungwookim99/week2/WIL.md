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