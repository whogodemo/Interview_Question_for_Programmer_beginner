def solution(lottos, win_nums):
    answer = []
    count = 0
    count_0 = 0
    #맞힌 개수 별 순위
    win = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    
    for l in lottos:
        if l == 0:
            count_0 += 1
        elif l in win_nums:
            count += 1
    return [win[count+count_0], win[count]]
    
    
    
    return answer
