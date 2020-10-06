class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in nums:
            if i==target:
                return nums.index(i)
        nums.insert(0,target)
        return sorted(nums).index(target)
        
