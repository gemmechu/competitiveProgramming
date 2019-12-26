from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
            lo, hi = 0, len(citations)
            while lo < hi:
                mid = (lo + hi) // 2
                if citations[~mid] > mid:
                    lo = mid + 1
                else:
                    hi = mid
            print(lo) 
a= Solution()
citations = [0,1,3,5,6]
