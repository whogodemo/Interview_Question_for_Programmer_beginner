import math
#k진수에서 소수 구하기
def change(n, k):
    string = ''
    q, r = divmod(n, k)
    if q == 0 :
        return string + str(r) 
    else :
        return change(q, k) + str(r)

def isprime(n):
    if n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
        
    return True
    
def solution(n, k):
    answer = 0
    change_k = change(n, k)
    
    p = change_k.split('0')
    
    p = [int(v) for v in p if v]
    
    for i in p:
        if isprime(i):
            answer += 1
    
    
    return answer
