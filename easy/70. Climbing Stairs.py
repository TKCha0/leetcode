n = 9
a1 = 1
a2 = 2
for i in range(n-2):
    if i%2 == 0:
        a1 = a1+a2
    else:
        a2 = a1+a2
if n%2 == 0:
    print(a2)
else:
    print(a1)
    