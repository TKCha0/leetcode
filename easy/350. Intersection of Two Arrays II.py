nums1 = [1,2,3,1]
nums2 = [2,2]
ans = []
if len(nums1) > len(nums2):
    for i in nums2:
        if i in nums1:
            ans.append(i)
            nums1.pop(nums1.index(i))
else:
    for i in nums1:
        if i in nums2:
            ans.append(i)
            nums2.pop(nums2.index(i))
