import math

# 소수 판별 함수
def is_prime_num(n):
    # 1일때 예외 처리
    if (n == 1) :
        return False
    
    sqrt_n = math.sqrt(n)
    sqrt_n = int(sqrt_n) 
    for i in range(2,sqrt_n +1):
        if n % i == 0:
            return False
    return True

# n 진법으로 바꾸는 함수 
def dec_to_n(k,n):
    rev_base = ''
    while k > 0:
        k, mod = divmod(k, n)
        rev_base += str(mod)
    return rev_base[::-1]

# main 함수
def solution(n, k):
    # 숫자를 k진수로 바꿈
    str_num = dec_to_n(n,k)
    
    # 0으로 토크나이징
    list_num = str_num.split('0')
    
    # 리스트를 int로 바꾼 뒤 소수 판별
    answer = 0
    for i in list_num:
        if i == '':
            continue
        if(is_prime_num(int(i))):
            answer = answer+1 
    
    return answer