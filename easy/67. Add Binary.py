a = "11"
b = "1"
num = 0
c = [int(i) for i in str(int(a)+int(b))]
d = ""
for i in range(len(c)-1,-1,-1):
    if c[i] + num < 2:
        c[i] += num
        num = 0      
        d = ""
    else:
        c[i] = c[i]+num-2
        num = 1
        d = "1"        
for i in c:        
    d += str(i)
#%%
x = str(bin(int(a,2)+int(b,2)))
       #bin 轉換成二進位
           #int(a,base) 從二進位變為十進位
                 #進制數 默認為十進位
print(x[2::])


        
    
    