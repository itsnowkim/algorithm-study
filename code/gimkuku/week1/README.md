## k진수에서 소수 개수 구하기


### 소수 구하기 함수
- 소수는 앞과 뒤가 *짝을 이루는 성질*이 있음


예 ) 36의 소수 : 2 - 18, 3 - 12, 6 - 6


-> 따라서 소수를 구하고 싶다면, N의 제곱근까지만 나누어 떨어지는지 확인하면 됨! 


```
def is_prime_num(n):
    # 제곱근 구하는 함수 : math.sqrt
    sqrt_n = math.sqrt(n)
    sqrt_n = int(sqrt_n) 
    for i in range(2,sqrt_n +1):
        if n % i == 0:
            return False
    return True
```


### N진법으로 바꾸는 함수
- 몫과 나머지를 구할 수 있는 함수 : divmod


```
몫, 나머지 = divmod(나눠지는 수, 나누는 수)
```
-> 따라서 divmod 함수를 반복하여 N진법을 구할 수 있음


```
def dec_to_n(k,n):
    rev_base = ''
    while k > 0:
        k, mod = divmod(k, n)
        rev_base += str(mod)
    return rev_base[::-1]
```


## 양궁대회


### 합이 N이 되는 길이 k의 배열


- 처음에 컴비네이션과 같은 편한 함수를 쓰려다가 실패함ㅎㅎ.. 
- 결국 재귀 + DP로 풀었음
- 합이 N이 되는 길이 k의 배열 = i + 합이 (N-i)가 되는 길이 (k-1)의 배열
```
def make_lion_list(n,k)
    # k가 1일때 =>  n번째 숫자가 정해졌을때 => 즉 모든 배열이 완성되었을 때 계산
    if (k == 1):
        calc (어쩌구)

    # 재귀 구문
    for i in range(n+1):
        calc_result, list_result = make_lion_list(n-i,k-1)
```


## 주차 요금 계산


### Dictionary 정리 
- 키 : 요소 로 이루어짐
- 쌍 추가하기 : dict[key] = value
```
a = {}
a[2] = 'b'
```
- 쌍 삭제하기 : del dict[key]
```
del dict[key]
```
- 키 값이 비어있는지 확인하기 
```
if time_dict.get(j[0]) == None:
    return empty
```


### float 올림 / 버림 / 반올림
- import math를 하여 함수 사용
```
# 올림
math.ceil(12.2) => 13
# 버림
math.floor(12.2) => 12
# 반올림 : round(실수, 반올림 자리수)
round(12.223,2) => 12.22
```