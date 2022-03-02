from collections import deque

n, m = map(int, input().split())
maze = []

for i in range(n):
    maze.append(list(map(int, input())))

queue = deque() #큐 선언
queue.append([0, 0]) #시작점 0,0
count = 0 #거리

while queue:
    #큐가 빌 때까지
    x, y = queue.popleft()

    if maze[x][y] == 1:
        #아직 방문하지 않았으면 0으로 바꿔줌
        maze[x][y] = 0
        count += 1

    if x+1 < n:
        if maze[x+1][y] == 1:
            #아래로 이동
            queue.append([x+1, y])

    if y+1 < m:
        if maze[x][y+1] == 1:
            #오른쪽으로 이동
            queue.append([x, y+1])

print(count)
