x = int(input()) #정수 x 입력

d = [0] * (x+1) #x까지의 결과를 저장하는 배열 d 초기화

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    #현재 수에서 1만큼 뺀 결과에 1을 더하는 것과 같다
    
    if i % 5 == 0:
      #5로 나누어 떨어지는 경우, d[i]는 d[i//5]+1과 d[i] 값을 비교해서 최솟값을 넣어준다.
        d[i] = min(d[i//5] + 1, d[i])
        
    if i % 3 == 0:
      #위와 마찬가지로, 3으로 나누어 떨어지는 경우
        d[i] = min(d[i//3] + 1, d[i])
        
    if i % 2 == 0:
      #2로 나누어 떨어지는 경우
        d[i] = min(d[i//2] + 1, d[i])

print(d[x])
    