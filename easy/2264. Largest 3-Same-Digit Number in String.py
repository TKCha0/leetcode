num = "6777133339"
check = [3*str(i) for i in range(9,-1,-1)]
for i in check:
    if i in num:
        print (i)
        break
    
#%%
num = "6777133339"
for i in range(9,-1,-1):
    if 3*str(i) in num:
        print(3*str(i))
        break


