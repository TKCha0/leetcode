nums = [9,6,4,2,3,5,7,0,1]
for i in range(len(nums)+1):
    if i not in nums:
        print(i)
        
#%%
print(sum(list(range(len(nums)+1))) - sum(nums))

