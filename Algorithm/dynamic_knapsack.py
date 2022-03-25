n, k = map(int, input().split())

thing = [[0,0]]
d = [[0] * (k+1) for _ in range(n+1)]
#최대 무게, 포함된 물건의 인덱스

for _ in range(n):
    w, v = map(int, input().split())
    thing.append([w, v])

for i in range(1, n+1):
    for j in range(k+1):
        d[i][j] = d[i-1][j]
        if j >= thing[i][0]:
            d[i][j] = max(d[i-1][j-thing[i][0]] + thing[i][1], d[i][j])
        
                          
print(d[n][k])
