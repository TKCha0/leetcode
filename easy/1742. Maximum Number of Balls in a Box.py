lowLimit = 19
highLimit = 28

box = {}
ballnumber = 0
for i in range(lowLimit,highLimit+1):
    for j in str(i):
        ballnumber += int(j)
    if ballnumber not in box:
        box[ballnumber] = 1
    else:
        box[ballnumber] += 1
    ballnumber = 0

return max(box.values())

