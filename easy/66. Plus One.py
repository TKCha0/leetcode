digits = [9,9,9]
num = ""
for i in digits:
    num += str(i)
num = str(int(num)+1)
for i in range(len(num)):
    if i+1 <= len(digits):
        digits[i] = int(num[i])
    else:
        digits.append(0)