nums = [2,2,1,1,1,2,2]
for i in set(nums):
    if nums.count(i) > len(nums)/2:
        print(i)
    
#%%
nums.sort()
print(nums[len(nums)//2])


