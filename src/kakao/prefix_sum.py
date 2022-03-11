def solution(board, skill):
    answer = 0
    n = len(board) #행
    m = len(board[0]) #열
    board_sum = [[0]*(m+1) for _ in range(n+1)] #누적합 저장하는 배열
    
            
    for ty_pe, r1, c1, r2, c2, degree in skill:
        if ty_pe == 1:
            board_sum[r1][c1] -= degree
            board_sum[r1][c2+1] += degree
            board_sum[r2+1][c1] += degree
            board_sum[r2+1][c2+1] -= degree
        else:
            board_sum[r1][c1] += degree
            board_sum[r1][c2+1] -= degree
            board_sum[r2+1][c1] -= degree
            board_sum[r2+1][c2+1] += degree
                    
    for i in range(n):
        for j in range(1, m):
            #누적합 구하기. 왼쪽에서 오른쪽으로
            board_sum[i][j] += board_sum[i][j-1] #O(n*m)
            
    for i in range(1, n):
        for j in range(m):
            #누적합 구하기. 위에서 아래로
            board_sum[i][j] += board_sum[i-1][j] #O(n*m)
    
    for i in range(n):
        for j in range(m):
            board[i][j] += board_sum[i][j] #O(n*m)
            if board[i][j] > 0:
                answer += 1
        
                    
        
    return answer
