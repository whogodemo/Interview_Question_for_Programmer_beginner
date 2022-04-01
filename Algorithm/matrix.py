def solution(rows, columns, queries):
    answer = []
    matrix = [[i+m*columns for i in range(1, columns+1)] for m in range(rows)]
    
    for q in queries:
        x1, y1, x2, y2 = q[0]-1, q[1]-1, q[2]-1, q[3]-1
        
        tmp = matrix[x1][y1]
        min_tmp = tmp
        
        x, y = x1, y1
        
        while x < x2:
            matrix[x][y] = matrix[x+1][y]
            min_tmp = min(min_tmp, matrix[x][y])
            x += 1
        
        while y < y2:
            matrix[x][y] = matrix[x][y+1]
            min_tmp = min(min_tmp, matrix[x][y])
            y += 1
        
        while x1 < x:
            matrix[x][y] = matrix[x-1][y]
            min_tmp = min(min_tmp, matrix[x][y])
            x -= 1
        
            
        while y1 < y:
            if y == y1+1:
                matrix[x][y] = tmp
            else:
                matrix[x][y] = matrix[x][y-1]
            min_tmp = min(min_tmp, matrix[x][y])
            y -= 1
            
        answer.append(min_tmp)
            
    
    return answer
