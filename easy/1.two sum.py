nums = list(eval(input()))
target = eval(input())
a = 0
for i in range(len(nums)):
    if a == 1:
        break
    else:    
        for j in range(len(nums)):
            if i == j :
                continue
            elif nums[i]+nums[j] == target:
                print([i,j])
                a = 1
                break
            else:
                continue
#%%
nums = list(eval(input()))
target = eval(input())  
numsmap = {}
for i in range(len(nums)):
    if target-nums[i] in numsmap:
        #if numsmap.__contains__(target-nums[i]):
        print([numsmap.get(target-nums[i]),i])        
    else:
        numsmap[nums[i]] = i

      
            
    




