grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# 4*1 - 2*k
ans = 0
for i,m in enumerate(grid):
    for j,n in enumerate(m):
        if n == 0:
            continue
        side = 4
        if j > 0 and grid[i][j-1] == 1:
            side -= 1
        if i > 0 and grid[i-1][j] == 1:
            side -= 1
        if j < len(grid[0])-1 and grid[i][j+1] == 1:
            side -= 1
        if i < len(grid)-1 and grid[i+1][j] == 1:
            side -=1            
        ans += side
        
        
            


    
        










            

    

    
    
    
    
    

