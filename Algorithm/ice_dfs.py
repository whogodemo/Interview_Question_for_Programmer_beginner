n, m = map(int, input().split())
ice = []

for i in range(n):
  ice.append(list(map(int, input())))
  
count = 0

def dfs(i, j):
  if i < 0 or i >= n or j < 0 or j >= m:
    #범위 벗어날 경우 리턴
    return False
  
  if ice[i][j] == 1:
    #얼음이 아닐 경우 리턴
    return False
  
  ice[i][j] = 1
  dfs(i+1, j)
  dfs(i, j+1)
  dfs(i-1, j)
  dfs(i, j-1)
  
  return True

for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      count += 1
      
print(count)
