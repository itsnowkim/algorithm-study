# 1. 순위 검색
## 참고
https://whwl.tistory.com/193 <br />
https://www.daleseo.com/python-collections-defaultdict/

정확성은 풀리는데 효율성이 풀리지 않아 검색해보고 풀었다.. 어렵다.<br />
`defaultdict`도 알고는 있었는데 사용은 처음 해봤다. 편리한 것 같다.

## 풀이
### 📁 주어진 입력 및 예시 이해
|이름|설명|예시|
|------|---|---|
|info|지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를 하나의 문자열로 구성한 값의 배열|["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]|
|query|개발팀이 궁금해하는 문의조건이 문자열 형태로 담긴 배열|["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]|

### 📁 솔루션 함수
함수 내 변수 설명
|이름|설명|예시|
|------|---|---|
|result|각 info, query가 매개변수로 주어질 때, 문의조건에 해당하는 사람들의 숫자를 순서대로 담은 배열|[1,1,1,1,2,4]|
|info_dict|지원자가 지원서에 입력한 4가지의 정보의 조합들과 그에 해당하는 사람의 점수가 담긴 딕셔너리|	defaultdict(<class 'list'>, {'': [50, 80, 150, 150, 210, 260], 'java': [80, 150], 'backend': [50, 80, 150, 260], 'junior': [80, 150], 'pizza': [150, 260], 'javabackend': [80, 150], 'javajunior': [80, 150], 'javapizza': [150], 'backendjunior': [80, 150], ...|
|info_key|지원자가 지원서에 입력한 4가지의 정보에 대한 배열|['java', 'backend', 'junior', 'pizza']|
|info_score|지원자가 획득한 코딩테스트 점수|150|
|tmp_key|지원자가 지원서에 입력한 4가지의 정보의 조합 중 하나|javabackend|
|query_score|개발팀이 원하는 코딩테스트 최소 점수|100|
|tmp_q|개발팀이 원하는 지원자의 정보 문자열|javabackendjuniorpizza|
|start, mid, end|이진 탐색에서 파생된 알고리즘으로 원하는 값 이상이 처음 나오는 위치를 찾는 `lower bound` 알고리즘을 사용하기 위한 변수들|0, (start + end) // 2, len(scores)|

```python
from itertools import combinations
from collections import defaultdict

def solution(info, query):
    result = []
    info_dict = defaultdict(list)
    for i in info:
        i = i.split()
        info_key = i[:-1]
        info_score = int(i[-1])
        for i in range(5):
            for c in combinations(info_key, i):
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_score)
    for key in info_dict.keys():
        info_dict[key].sort()

    for q in query:
        q = q.split()
        query_score = int(q[-1])
        q = q[:-1]

        for i in range(3):
            q.remove('and')
        while '-' in q:
            q.remove('-')
        tmp_q = ''.join(q)

        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                result.append(len(scores) - start)
        else:
            result.append(0)
    return result
```
<br />
