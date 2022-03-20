import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
#n가지 코인개수. m원을 만들어야함
coin = []
#코인 종류 저장

for _ in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))

coin.sort()

won = [10000] * (m+1)
#won[i] = i원을 만들기 위해 필요한 최소 동전 개수

for i in coin:
  #i라는 코인이 있으면서 m원보다 작으면 won[i] = 1
    if i <= m:
        won[i] = 1

for i in range(m+1):
    if won[i] != 10000:
        continue
    
    for j in coin:
      #j원이라는 코인에 대해
        if 0 <= i-j <= m:
            if won[i-j] != 10000:
              #i-j원을 만들 수 있으면
                won[i] = min(won[i-j]+1, won[i])

if d[m] == 10000:
  #만들 수 없는 경우 -1 출력
    print(-1)
else:
    print(d[m])
