s = "[]{}()[[(})]]"
dic = {"(" : ")" , "[" : "]" , "{" : "}"}
stack = []
for i in s:
    if i in dic:
        stack.append(i)
    elif i not in dic:
        if len(stack) != 0:
            if i == dic.get(stack[-1]):
                stack.pop(-1)
            else:
                print(False)
                break       
        else:
            print(False)
            break
if len(stack) == 0:
    print (True)
else:
    print (False )

    
