from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    info.reverse()
    #info[i] = 어피치가 i점을 맞힌 화살 개수
    
    if info[10] == n:
        #10점만 어피치가 n번 쏜 경우 라이언은 절대 이길 수 없음
        return [-1]
    
    score = 0 #라이언과 어피치의 점수차
    
    for c in combinations_with_replacement([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n):
        ryan = 0
        apeach = 0
        r = [0] * 11
        #r[i] = 라이언이 i점을 맞힌 화살 개수
        
        for i in range(n):
            r[c[i]] += 1 
            
        for i in range(11):
            if info[i] == 0 and r[i] == 0:
                continue
            elif r[i] <= info[i]:
                #똑같이 쏘거나 어피치가 더 많이 쏘는 경우
                apeach += i
            else:
                ryan += i
                
        if score < ryan - apeach:
            answer = r
            #정답에 r 저장
            score = ryan - apeach
            #점수 차이 저장
    
    if score <= 0:
        #라이언이 이기지 않는 경우
        return [-1]
    
    answer.reverse()
    #다시 뒤집어줘야 함
    
    return answer
