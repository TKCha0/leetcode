nums1 = [1,2,7,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
stay = [200]
for i in range(n):
    nums1[-(i+1)] = 200            
for i in range(m+n):
    if n == 0:
        break
    elif min(nums2) < min(stay) and min(nums2) < nums1[i]:
        stay.append(nums1[i])
        nums1[i] = min(nums2)
        nums2[nums2.index(min(nums2))] = 200
    elif min(nums2) >= min(stay) and min(stay) < nums1[i]:
        stay.append(nums1[i])
        nums1[i] = min(stay)
        stay.pop(1) 
#%% 超時
nums1 = [1,2,7,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
stay = []
for i in range(n):
    nums1[-(i+1)] = nums2[n-(i+1)]
while nums1 != sorted(nums1):
    for i in range(m+n-1):
        if nums1[-(i+1)] < nums1[-(i+2)]:
            stay.append(nums1[-(i+1)])
            nums1[-(i+1)] = nums1[-(i+2)]
            nums1[-(i+2)] = stay[0]
            stay.pop()
            break
