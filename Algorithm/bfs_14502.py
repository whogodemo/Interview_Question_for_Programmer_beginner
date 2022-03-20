from collections import deque
from itertools import combinations
import sys
import copy

n, m = map(int, sys.stdin.readline().rstrip().split())

#상하좌우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def virus(loc):
    #loc값이 변하는 것을 피하기 위해
    real_loc = copy.deepcopy(loc)
    
    q = deque()

    for i in range(n):
        for j in range(m):
            if real_loc[i][j] == 2:
                q.append([i, j])
                while q:
                    x, y = q.popleft()

                    for d in range(4):
                        x += dx[d]
                        y += dy[d]

                        if 0 <= x < n and 0 <= y < m:
                            if real_loc[x][y] == 0:
                                real_loc[x][y] = 2
                                q.append([x, y])

                        x -= dx[d]
                        y -= dy[d]

    count = 0
    for i in range(n):
        for j in range(m):
            if real_loc[i][j] == 0:
                count += 1


    return count

loc = []
#연구소 정보 입력받기

for _ in range(n):
    loc.append(list(map(int, sys.stdin.readline().rstrip().split())))

#안전지대 개수
safe = virus(loc)


index = []
#0인 연구소의 인덱스를 저장

for i in range(n):
    for j in range(m):
        if loc[i][j] == 0:
            index.append([i, j])
            

#연구소 3개 선택해서 벽을 세워보기
for x, y, z in combinations(index, 3):
    loc[x[0]][x[1]] = 1
    loc[y[0]][y[1]] = 1
    loc[z[0]][z[1]] = 1

    safe = max(safe, virus(loc))

    #연구소 다시 0으로 저장
    loc[x[0]][x[1]] = 0
    loc[y[0]][y[1]] = 0
    loc[z[0]][z[1]] = 0

print(safe)

