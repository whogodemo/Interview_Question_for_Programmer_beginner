import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
#n가지 종류의 코인, m원을 만들어야 함
coin = []
coin.sort()
for _ in range(n):
  #코인 입력받기
    coin.append(int(sys.stdin.readline().rstrip()))

won = [-1] * (m+1)
#i원을 만들기 위해 필요한 코인 개수

for i in coin:
    if i <= m:
        won[i] = 1

for i in range(m+1):
    if won[i] == 1:
        continue

    for j in coin:
      #코인 j에 대해서
        if 0 <= i-j <= m:
          #i-j원을 만들 수 있으면 i-j원을 만드는 코인 개수 + 1
            if won[i-j] != -1:
                won[i] = won[i-j] + 1

print(won[m])
