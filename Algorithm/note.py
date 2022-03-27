# 문자열

string = "Hello"

# 대문자로 변환
# HELLO
string.upper()

# 소문자로 변환
# hello
string.lower()




string = "My favorite song is snowman by sia"

# string.replace(문자열1, 문자열2)
# 문자열1을 문자열2로 변환

# My favorate song as snowman by saa
string.replace("i", "a")

# 삭제할 수도 있다
# My favorite  is snowman by sia
string.replace("song", "")

# 공백 삭제
# Myfavoritesongissnowmanbysia
string.replace(" ", "")





# find
# 찾는 문자열이 처음 나오는 위치 리턴
# 없을 경우 -1 리턴

string = "My favorite song is snowman by sia"
# 17
string.find("is")

# -1
string.find("maroon")





string = "My favorite song is snowman by sia"

# 슬라이싱
# 문자열에서 원하는 부분만 추출 할 수 있다.
# string[start: end] start ~ (end - 1)까지 슬라이싱

# 생략 할 경우 처음과 끝이 들어간다.
# My favorite song is snowman by sia
string[:]

# 5번째 부터 끝까지
# vorite song is snowman by sia
string[5:]

# 처음 부터 9번째 까지
# My favorit
string[:10]

# My
string[0:2]

# 음수도 가능하다. 끝에서 부터 -1
# My favorite song is snowman by s
string[:-2]
#끝에 두개 빼고

# 세번째 인수를 생략하지 않은 경우 step으로 작용

# 2개씩 step
# M aoiesn ssomnb i
string[::2]

# Reverse
# ais yb namwons si gnos etirovaf yM
string[::-1]






string = "       Hello World!       "

# 공백 제거

# strip() - 양쪽 공백제거
# Hello World!
string.strip()

# lstrip() - 왼쪽 공백제거
# Hello World!        
string.lstrip()

# rstrip() - 오른쪽 공백제거
#        Hello World!        
string.rstrip()






string = "apple banana kiwi tomato"

# 분리
# split(문자열) 문자열을 기준으로 분리 
# 생략할 경우 공백을 기준으로 분리함
# 리턴되는 결과는 리스트

# ['apple', 'banana', 'kiwi', 'tomato']
string.split()


li = ["apple", "banana", "kiwi", "tomato"]
# 결합(리스트를 문자열로 결합)
# 문자열.join(리스트) - 리스트 원소 사이에 문자열을 삽입

# 공백을 삽입
# apple banana kiwi tomato
" ".join(li)

li = [1, 2, 3, 4]
####### 리스트의 원소는 모두 str 타입이어야 한다. 아닐경우 오류발생
######## 오류발생!
" ". join(li)





#문자열 구성 확인
ex1 = 'Abcd'
ex2 = ' aB'

print(ex1.isalpha())
#True
#대문자 소문자로만 이루어져있는지 확인

print(ex2.isalpha())
#False
#공백 포함되면 안됨

ex3 = '123456'
print(ex3.isdigit())
#True
#숫자로만 구성

ex4 = 'hello3'
print(ex4.isalnum())
#True
#숫자와 문자열로만 구성되어있는지 확인. 한글도 가능

ex5 = '안녕'
print(ex5.isalnum())
#True
#########한글도 True



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


