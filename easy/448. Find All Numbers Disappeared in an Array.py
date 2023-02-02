nums = [4,3,2,7,8,2,3,1]
nums2 = set(i for i in range(1,len(nums)+1))
print(nums2 - set(nums))

#%%
nums = [4,3,2,7,8,2,3,1]
ans = []
for i in nums:
    nums[abs(i)-1] = -abs(nums[abs(i)-1])
for i in range(len(nums)):
    if nums[i] > 0:
        ans.append(i+1)
        
















    
    
