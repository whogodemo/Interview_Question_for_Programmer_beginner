def istrue(answer):
    #조건 모두 만족하는지 확인
    
    for x, y, stuff in answer:
        if stuff == 0:
            #기둥
            if y == 0:
                #바닥 위에 있는 경우
                continue
            
            if [x-1, y, 1] in answer or [x, y, 1] in answer:
                #보 위에 있는 경우
                continue
            if [x, y-1, 0] in answer:
                #기둥 위에 있는 경우
                continue
                
            return False
        else:
            #보
            
            #기둥 위에 있는 경우
            if [x, y-1, 0] in answer:
                continue
            if [x+1, y-1, 0] in answer:
                continue
            
            
            #양쪽 끝에 보가 있는 경우
            if [x-1, y, 1] in answer and [x+1, y, 1] in answer:
                continue
                
            return False
            
    return True
    
    
def solution(n, build_frame):
    answer = []
    #frame = [[] * (n+1)] * (n+1)
    #print(frame)
    
    for build in build_frame:
        x, y, stuff, operate = build
        frame = build[:3]
        
        if operate == 0:
            #삭제
            #일단 삭제
            answer.remove(frame)
            #조건 만족하는지 확인
            if istrue(answer) == False:
                answer.append(frame)
            #만족하지 않으면 다시 지음
        else:
            #설치
            answer.append(frame)
            #일단 설치
            if not istrue(answer):
                answer.pop()
            #조건 맞는지 확인
            #만족하지 않으면 삭제
            
    result = sorted(answer)
    
    return result
