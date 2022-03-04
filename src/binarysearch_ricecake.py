n, m = map(int, input().split()) #떡 개수와 필요한 떡 길이 입력받기
rice = list(map(int, input().split())) #떡 길이 배열 생성

start = 0
end = max(rice)

result = 0

#이진 탐색 수행
while(start <= end):
    total = 0
    mid = (start + end) // 2
    
    for x in rice:
        if x > mid: #총 떡의 양 계산
            total += x - mid

    if total < m: #떡의 양이 부족하면 더 많이자르기. 왼쪽 부분 탐색
        end = mid - 1
    else: #떡의 양이 충분하면 덜 자르기. 오른쪽 부분 탐색
        result = mid
        start = mid + 1

print(result)
