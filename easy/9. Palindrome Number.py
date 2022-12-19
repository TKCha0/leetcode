num = 121
num = str(num)
a = 1
for i,j in zip(range(len(num)),range(len(num)-1,-1,-1)):
    if num[i] == num[j]:
        continue
    else:
        a = 1
        print(False)
        break
if a == 0:
    print(True)
