rowIndex = 7
row = []
tri = []
for i in range(1,rowIndex+2):
    for j in range(i):
        row.append(1)
        for k in range(1,j):
            row[k] = tri[j-1][k-1] +tri[j-1][k]    
    tri.append(row)
    row = []

#%%
rowIndex = 3
if rowIndex == 0:
    print([1])
ans = [1,1]
for i in range(rowIndex-1):
    temp = [1]
    for j in range(len(ans)-1):            
        temp.append(ans[j]+ans[j+1])
    temp.append(1)
    ans = temp
print (ans)











