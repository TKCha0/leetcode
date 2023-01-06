nums = [0,1,0,3,12]
for i in range(nums.count(0)):
    nums.pop(nums.index(0))
    nums.append(0)

#%%
l = 0 #定位最前面的零
for r in range(len(nums)):
    if nums[r]: 
        nums[l], nums[r] = nums[r], nums[l] 
        #跟零交換或跟自己交換
        l += 1
        
        


