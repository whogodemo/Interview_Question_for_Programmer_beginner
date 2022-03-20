from collections import deque

n, m = map(int, input().split())
gamemap = [i for i in range(101)] #게임판. i번째 칸에는 i로 이동
distance = [0] * 101 # 1번부터 해당칸까지의 거리

for i in range(n+m):
    x, y = map(int, input().split())
    gamemap[x] = y #게임판. 사다리가 있으면 x번째 칸에서 y로 이동
    
p = 1 #1에서 시작
queue = deque([p])

while p != 100:
    #1~6 까지 중에 선택.
    #100에 도착할 때까지
    p = queue.popleft()

    for j in range(1, 7):
        dice = p+j
        
        if dice <= 100:
            move = gamemap[dice]
            #dice의 이동위치 = move
            
            if distance[move] == 0:
                #아직 move를 지나가지 않은 경우
                queue.append(move)
                distance[move] = distance[p] + 1

print(distance[100])
