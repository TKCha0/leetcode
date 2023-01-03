nums = [1,2,3,1,2,3]
k = 2
dic = {}
for i in len(nums):
    if nums[i] in dic and i-dic[nums[i]] <= k:
        return True
    dic[nums[i]] = i
return False
