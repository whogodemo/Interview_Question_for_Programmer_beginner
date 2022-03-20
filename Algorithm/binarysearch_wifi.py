import sys
n, c = map(int, sys.stdin.readline().split())

#집의 개수와 공유기의 개수 입력
home = []

#집의 위치 입력받기
for _ in range(n):
    home.append(int(sys.stdin.readline()))

home.sort()

start = 1 
#공유기 거리의 최소값은 늘 1
end = home[-1] - home[0] 
# 공유기 거리의 최대값. 
result = 0

while start <= end:
    gap = (start + end)// 2 
    #중간값으로 gap 설정
    count = 1 
    #home[0]에 설치하므로 count는 1부터 시작
    install = 0 
    #0에 설치
    
    for i in range(n): #공유기 설치
        if home[i] - home[install] >= gap:
          #이미 설치된 install 과 i 사이의 거리가 gap보다 크면 설치. 
            install = i
            count += 1

    if count < c:
      #설치 불가능. gap 줄여야함. end를 gap-1로 설정
        end = gap-1
        continue

    else:
      #설치 가능. gap의 값을 저장해둔 뒤 gap이 증가해도 설치가 가능한지 확인해야함
        start = gap + 1
        result = gap


print(result)
