nums = [4,1,2,1,2]
for i in set(nums):
    if nums.count(i) == 1:
        break

#%%
nums = [4,1,2,1,2]
print(sum(2*list(set(nums))) - sum(nums))
