nums = [0,1,2,4,6,7]
head = 0
tail = 1
ans = []
while tail <= len(nums):
    if tail == len(nums):
        if nums[head] != nums[tail-1]:
            range_ = str(nums[head])+"->"+str(nums[tail-1])
            ans.append(range_)
            head = tail
            tail += 1
        else:
            ans.append(str(nums[head]))
            head = tail
            tail += 1   
    elif nums[tail]-1 == nums[tail-1]:
        tail += 1
    elif nums[head] != nums[tail-1]:
        range_ = str(nums[head])+"->"+str(nums[tail-1])
        ans.append(range_)
        head = tail
        tail += 1
    else:
        ans.append(str(nums[head]))
        head = tail
        tail += 1
        
        
        