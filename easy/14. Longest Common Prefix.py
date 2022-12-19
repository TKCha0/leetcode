#Time Limit Exceeded
strs = ["flower","flow","flight"]
a = ""
b = strs[0]
c = 0
d = 0
while True:    
    for i in range(1,len(strs)):
        if c+1 > len(strs[i]):
            b =0
            break
        elif strs[i][c] == b[c]:
            d += 1
            if d == len(strs)-1:
                a += b[c]                 
        else:
            b = 0
            break
    c += 1
    d = 0
    if b == 0:
        break
print(a)
#%%
strs = ["flower","flow","flight"]
ans=""
b = min(strs)
c = 0
for i in range(len(b)):
    for j in strs:
        if i+1 > len(j):     
            c = 1
            break
            # return ans
        if j[i] != b[i]:    
            c = 1
            break
            # return ans
    ans = b[:i]
    if c == 1:
        break
    











            
        
    
    


