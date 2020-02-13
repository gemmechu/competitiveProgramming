from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j+1])
nums = [-2, 0, 3, -5, 2, -1]
main=NumArray(nums)

print(main.sumRange(0,0))