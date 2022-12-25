numRows = 7
row = []
tri = []
for i in range(1,numRows+1):
    for j in range(i):
        row.append(1)
        for k in range(1,j):
            row[k] = tri[j-1][k-1] +tri[j-1][k]    
    tri.append(row)
    row = []