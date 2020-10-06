import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
       
        largest = heapq.nlargest(k,nums)
       
        return largest[-1]
