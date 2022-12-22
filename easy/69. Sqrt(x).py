x = 200
guess = 5
#運用牛頓迭代法
while True:
    p = int(guess)
    q = p+1
    guess = (guess + x/guess)/2
    if p**2 <= x and q**2 > x:
        break
print(int(guess))
                              