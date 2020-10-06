
def largestNumber(nums):
    result = ''
    if len(nums) ==0:
        return False
    if len(nums) == 1:
        return str(nums[0])
    def is_greater(a, b):
        return
    length = len(nums)
    for i in range(length):
        prev = nums[0]
        index = 0
        for j in range(1,len(nums)):
            curr = nums[j]
            if(is_greater(curr,prev)):
                index = j
        result += str(nums[index])
        nums.pop(index)
    return result
    
print(23//10)
        