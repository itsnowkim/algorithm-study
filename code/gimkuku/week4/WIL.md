## 순위 검색
- dictionary와 이진 탐색을 활용해야 하는 문제
- "-" 를 처리하기 위해 처음에는 - 가 나오면 다른 곳도 탐색하도록 코드를 짰었는데, 그냥 넣을때부터 - 도 넣어주는게 편하다는 것을 나중에 알았다

```
for i in info:
        lang, part, career, food, score = i.split()
        for _lang in [lang, "-"]:
            for _part in [part, "-"]:
                for _career in [career, "-"]:
                    for _food in [food, "-"]:
                        recruit_dict[_lang+_part+_career+_food].append(int(score))
```
- dictionary의 키값은 string 도 된다. 
    - 뭔가 키 값은 Int여야 할 것 같아서 처음에 3진수로 바꾸어서 풀었는데 정말 부질없는 짓이었음 


### 이진 탐색
> 이진 탐색이란 : 
>
> sort된 배열의 키값을 중앙으로 잡고, 찾는 값이 키값보다 크면 키값 오른쪽을 배열로 잡고 재 탐색, 작으면 왼쪽을 배열로 잡고 재탐색 한다.
```
low = 0
    high = len(query_list)
    while low < high:
        mid = (low + high) // 2
        if int(score) <= query_list[mid]:
            high = mid
        else:
            low = mid+1
```
- 외워두자.. 
- 근데 항상 미묘한 = 이나 +1 차이로 틀린다.. 완벽하게 이해를 못한듯.. 특히 중복되는 값이 허용이 되는지 여부에 따라 조금씩 달라지는 듯 하다. ㅠㅠ 


## 합승 택시 요금
- 이상한 부분으로 한참을 헤맸던 문제
- 풀고나니 생각보다 간단해서.,. 실력이 언제 늘라나.. 싶었음..  
- 플루이드 워셜 알고리즘을 사용하여 풀었다


### 플루이드 워셜
> 플루읻드 워셜 알고리즘? 
>
> A -> B로 이동한다 했을 때, A->1->B, A->2->B ... , A->N->B 로 모든 정점을 중간 노드라고 가정했을때의 최소값을 찾는다. 그게 A->B 의 최소값으로 업데이트
> 
> A->C 로 이동한다고 했을 때, A->1->C, ..., A->B->C 를 계산할 때 아까 구한 A->B의 최소값을 이용하여 구한다.
>
> 이런식으로 최소값 하나를 구하면 계속 그걸 이용해서 다른 최소값을 구하는 알고리즘
```
for nextnode in range(n):
    for i in range(n):
        for j in range(n):
            if i==j : continue
            if dist[i][nextnode] != maxnum and dist[nextnode][j] != maxnum:
                    dist[i][j] = min(dist[i][j], dist[i][nextnode] + dist[nextnode][j])
                    dist[j][i] = dist[i][j] 
```
- 근데 여기서 for문 순서에 있어서 Nextnode가 맨위에 있지 않으면 오답이다. (i,j 순서는 상관없음)
    - 내가 고찰한(?) 이유
    1. 중간 노드 별 i->j 의 최소값이 계속 업데이트가 되어야 함
    2. 이전의 i->j의 최소값이 정해지지 않은 상태에서 중간노드가 바뀌면, 다음의 i->j 가 최소인지를 확신할 수 없음
 


## 광고 삽입
- 예전에 풀었던 문제에서 나왔던 누적합 개념을 써먹어서 너무 기쁨!!!!취준 코테에도 나오면 좋겠다^^* 
- 근데 누적합을 써도 시간 초과가 나와서 이게 아닌가 했는데
- adv(광고 길이) 단위로 계속 합치는 것이기 때문에 dp로 더해주었더니 풀림
- 중간에 몇개가 틀리는데 이유를 모르겠어서 검색해봤더니 끝나는 시간 미만으로 생각해야 한다해서 +1 붙였던 것들을 뺐더니 맞았다.


```
for i in logs:
        stt, fin = i.split("-")
        stt = stringtotime(stt)
        fin = stringtotime(fin)
        time_dict[stt] += 1 #시작위치에 +1
        time_dict[fin] -= 1 #끝나는위치+1에 -1

for i in range(1,end+1):
    time_dict[i] = time_dict[i] + time_dict[i-1]
```