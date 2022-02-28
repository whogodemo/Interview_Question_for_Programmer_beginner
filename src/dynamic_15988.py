t = int(input()) #입력받을 정수 개수
n = [] #정수 입력받을 배열

for _ in range(t):
  #t개만큼 정수 저장
    n.append(int(input()))
    
max_n = max(n)
result = [0] * (max_n+1)
#다이나믹 프로그래밍을 위해 결과를 저장하는 배열 생성

result[1] = 1 #1= 1. 따라서 1개
result[2] = 2 #2= 2. 따라서 2개
result[3] = 4 #3= 1+1+1, 3= 2+1, 3= 1+2, 3= 3. 따라서 4개


for i in range(4, max_n+1):
  #result[i] = result[i-1] + result[i-2] + result[i-3]이고 메모리 초과 방지를 위해 10000009로 나눠준다.
    result[i] = (result[i-1] + result[i-2] + result[i-3])%1000000009

for i in range(t):
    print(result[n[i]])
