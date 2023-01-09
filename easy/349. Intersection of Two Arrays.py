nums1 = [1,2,2,1]
nums2 = [2,2]
ans = []
for i in set(nums1):
    if i in nums2:
        ans.append(i)
    
#%%
a = set(nums1) & set(nums2)
    