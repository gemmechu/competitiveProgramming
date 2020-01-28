from typing import List
class Solution:
    def findDuplicate(self,nums: List[int])-> int:
        summation= sum(nums)
        n=len(nums)
        return summation- ((n-1)*n)/2

s= Solution()
print(int(s.findDuplicate([1,3,4,2,2])))