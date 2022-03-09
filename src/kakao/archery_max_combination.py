from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    real_answer = []
    info.reverse()
    
    if info[10] == n:
        return [-1]
    
    com = combinations_with_replacement([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n)
    
    result = 0
    
    for c in com:
        ryan = 0
        apeach = 0
        r = [0] * 11
        
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
        score = ryan - apeach
        #점수 차이 저장
        if score <= 0:
            continue
            
        if score >= result:
            result = score
            #max 점수 차 저장
            answer.append([r, score])
        
    answer.sort(key = lambda x:-x[1])
    #점수값 높은 순으로 내림차순
    
    max_score = answer[0][1]
    
    
    for i in answer:
        if i[1] == max_score:
            real_answer.append(i[0])
    
    real_answer.sort()
    
    return list(reversed(real_answer[-1]))
