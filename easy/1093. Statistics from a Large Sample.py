count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

dic = {}
for i in range(len(count)):
    if count[i] > 0:
        dic[i] = count[i]

minimum = float(min(dic.keys()))
maximum = float(max(dic.keys()))

total = 0
amount = 0
for i,j in dic.items():
    total += i*j
    amount += j
mean = round(total/amount,5)

med_head = (amount-1)//2+1
for i,j in dic.items():
    if med_head - j > 0:
        print(med_head)
        med_head -= j
        print(med_head,i,j)
    else:    
        med_head = i
        break
        
med_tail = (amount-1)//2+1
for i,j in reversed(dic.items()):
    if med_tail - j > 0:
        med_tail -= j
    else:
        med_tail = i
        break

median = float((med_head+med_tail)/2)

mode = float(max(dic,key=dic.get))





