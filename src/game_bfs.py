from collections import deque

n, m = map(int, input().split())
gamemap = [i for i in range(101)] #게임판. i번째 칸에는 i로 이동
distance = [0] * 101 # 1번부터 해당칸까지의 거리

for i in range(n+m):
    x, y = map(int, input().split())
    gamemap[x] = y #게임판. 사다리가 있으면 x번째 칸에서 y로 이동
    
p = 1
queue = deque([p])

while p != 100:
    #1~6 까지 중에 선택.
    #100에 도착할 때까지
    p = queue.popleft()

    for j in range(1, 7):
        if p+j <= 100:
            if distance[gamemap[p+j]] == 0:
                queue.append(gamemap[p+j])
                distance[gamemap[p+j]] = distance[p] + 1

print(distance[100])
