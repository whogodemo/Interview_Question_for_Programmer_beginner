def rotate(key):
    #90도 회전
    n = len(key)
    m = len(key[0])
    
    result = [[0]*n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = key[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock)//3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0 for _ in range(n*3)] for _ in range(n*3)]
    
    #i = m-1
    #j = m-1
    #new_lock[i][j]
    
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 1:
                new_lock[i+n][j+n]=1
    
    for rotation in range(4):
        key = rotate(key)
        for x in range(n*3-m): #답지에는 2n까지 확인하는 것으로 되어있는데 나는 정확한 완전 탐색을 테스트해봤다.
            for y in range(n*3-m):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                
                if check(new_lock) == True:
                    return True
                
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    
    return False
