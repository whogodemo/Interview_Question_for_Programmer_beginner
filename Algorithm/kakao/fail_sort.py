def solution(N, stages):
  #오름차순 정렬
    stages.sort()
    length = len(stages)
    fail = {x:0 for x in range(1, N+1)}
    #x에 대한 실패율 저장
    
    for i in range(1, N+1):
      #i에 머물러 있는 사람 수 저장
        not_clear = stages.count(i)
        if length != 0:
            fail[i] = not_clear / length
        else:
            fail[i] = 0
            
        length -= not_clear
    
            
    return sorted(fail, key = lambda x:fail[x], reverse = True)
