import time
T = input()
grid = []
n = 0
m = 0
M = 0

def gridhop(x,y):
    num = grid[y][x]
    
    if y - 1 >= 0 and grid[y-1][x] == num - 1:
        grid[y][x] = M + 1
        y = y-1
        return x,y
    elif x - 1 >= 0 and grid[y][x-1] == num - 1:
        grid[y][x] = M + 1
        x = x-1
        return x,y
    elif x + 1 < m and grid[y][x+1] == num - 1:
        grid[y][x] = M + 1
        x = x+1
        return x,y
    elif y + 1 < n and grid[y+1][x] == num - 1:
        grid[y][x] = M + 1
        y = y+1
        return x,y
    
    if y - 1 >= 0 and grid[y-1][x] == M + 1:
        grid[y][x] = M + 1
        grid[y-1][x] = num - 1
        y = y-1
        return x,y
    elif x - 1 >= 0 and grid[y][x-1] == M + 1:
        grid[y][x] = M + 1
        grid[y][x-1] = num - 1
        x = x-1
        return x,y
    elif x + 1 < m and grid[y][x+1] == M + 1:
        grid[y][x] = M + 1
        grid[y][x+1] = num - 1
        x = x+1
        return x,y
    elif y + 1 < n and grid[y+1][x] == M + 1:
        grid[y][x] = M + 1
        grid[y+1][x] = num - 1
        y = y+1
        return x,y

    return m, n       
    

for x in range(T):
    blank = raw_input()
    n, m = raw_input().split()
    n = int(n)
    m = int(m)

    grid[:] = []
    for i in range(n):
        grid.append( map(int, raw_input().split()))

    M = 0
    mx = 0
    my = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] > M:
                print grid
                M = grid[i][j]
                mx = j
                my = i
                
    print '_____'
    print M, mx, my
    print '_____'
    
    while grid[my][mx] > 0:
        mx, my = gridhop(mx,my)
        print grid[0]
        print grid[1]
        print '---'
        if mx == m and my == n:
            break
        time.sleep(1)
        
    works = True
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and grid[i][j] < M + 1:
                works = False
                
    print 'Case #' + str(x+1) + ':'
    if works:
        print 'YES'
    else:
        print 'NO'

    
