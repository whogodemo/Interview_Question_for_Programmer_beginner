
# 배열

#일차원 배열 정렬
lst = [2, 3, 5, 6, 1, 4]
lst.sort()
lst.sort(reverse=True) #내림차순
#결과는 반환하지않고 정렬된 결과 배열에 저장됨

lst = ["one", "two", "three", "four"]
lst.sort(key=len) #len함수 결과를 이용해 정렬
print(lst)
# ['one', 'two', 'four', 'three']

sorted(lst)
#정렬된 배열 반환


#리스트 컴프리헨션

array = [i for i in range(20) if i%2 == 0]
print(array)
#[2,4,6,8,10,12,14,16,18]

n = 3
m = 4
array = [[0]*m for _ in range(n)]
#이차원 배열 초기화
print(array)
#[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]



#이차원 배열 정렬
lst = [[2, 1], [3, 4], [1, 2], [1, 3], [3, 2]]
lst.sort()
print(lst)
# [[1, 2], [1, 3], [2, 1], [3, 2], [3, 4]]
# 그냥 정렬해도 0인덱스에 대해 오름차순 정렬 후 1인덱스에 대해 오름차순 정렬되는 것을 볼수 있음.


lst = [[2, 1], [3, 4], [1, 2], [1, 3], [3, 2]]
lst.sort(key=lambda x:x[0]) #0인덱스에 대해 정렬 명시
print(lst)
# [[1, 2], [1, 3], [2, 1], [3, 4], [3, 2]]

lst = [[2, 1], [3, 4], [1, 2], [1, 3], [3, 2]]
lst.sort(key=lambda x: (x[0], -x[1])) #0인덱스에 대해 오름차순 정렬 후 1인덱스에 대해 내림차순 정렬
print(lst)
# [[1, 3], [1, 2], [2, 1], [3, 4], [3, 2]]


# 딕셔너리

#빈 딕셔너리 선언
d = {}
#키-value 저장
d['1'] = 1

#딕셔너리 선언
di = {'abc' : 1, 'def' : 2}
#인덱스로는 접근 불가. key로만 접근 가능 & value 변경 가능
d['abc'] = 5

#딕셔너리 정렬

dic = {
    2: 1,
    3: 4,
    5: 2,
    1: 3,
    4: 1
}
x = sorted(dic.items(), key=lambda x:x[0])
print(x)

# [(1, 3), (2, 1), (3, 4), (4, 1), (5, 2)]



# 진수 변환

def change(n, k):
    #10진수를 k 진수로 변환. 결과는 string
    string = ''
    q, r = divmod(n, k)
    if q == 0 :
        return string + str(r) 
    else :
        return change(q, k) + str(r)

      
      
#n진수를 10진수로 변환
string = '101'
print(int(string, 2))
# 20
# 결과는 string



print(bin(11)) # 0b1011
print(oct(11)) # 0o13
print(hex(11)) # 0xb

#진법 표시 지우기
print(bin(11)[2:])
print(oct(11)[2:])
print(hex(11)[2:])


# 소수 판별

import math
def isprime(n):
    #n이 소수인지 판별하는 알고리즘
    if n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
        
    return True

  
# 순열과 조합

import itertools
data = [1, 2, 3]

for x in itertools.permutations(data, 2): #순열
  print(list(x))
# [1, 2]
# [1, 3]
# [2, 1]
# [2, 3]
# [3, 1]
# [3, 2]

for x in itertools.combinations(data, 2): #조합
  print(list(x), end=' ')
# [1, 2] [1, 3] [2, 3]

#중복순열

for i in product([1,2,3],'ab'):
    print(i, end=" ")
# (1, 'a') (1, 'b') (2, 'a') (2, 'b') (3, 'a') (3, 'b')

#중복해서 2개 뽑는 순열
for i in product([1,2,3], repeat=2):
    print(i, end=" ")
#(1, 1) (1, 2) (1, 3) (2, 1) (2, 2) (2, 3) (3, 1) (3, 2) (3, 3)

#중복해서 3개 뽑는 순열

for i in product([1,2,3], repeat=3):
    print(i, end=" ")
# (1, 1, 1) (1, 1, 2) (1, 1, 3) (1, 2, 1) (1, 2, 2) (1, 2, 3) (1, 3, 1) (1, 3, 2) (1, 3, 3) (2, 1, 1) (2, 1, 2) (2, 1, 3) (2, 2, 1) (2, 2, 2) (2, 2, 3) (2, 3, 1) (2, 3, 2) (2, 3, 3) (3, 1, 1) (3, 1, 2) (3, 1, 3) (3, 2, 1) (3, 2, 2) (3, 2, 3) (3, 3, 1) (3, 3, 2) (3, 3, 3) 


#중복조합
for cwr in combinations_with_replacement([1,2,3,4], 2):
  #중복해서 2개 뽑기
    print(cwr, end=" ")
# (1, 1) (1, 2) (1, 3) (1, 4) (2, 2) (2, 3) (2, 4) (3, 3) (3, 4) (4, 4)




# bfs/ dfs


