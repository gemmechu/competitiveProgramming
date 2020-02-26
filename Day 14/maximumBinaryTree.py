# Definition for a binary tree node.
from typing import List


class TreeNode:
 def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        root = TreeNode(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:nums.index(max(nums))])
        root.right = self.constructMaximumBinaryTree(nums[nums.index(max(nums)) + 1:])
        return root
a = [3,2,1,6,0,5]
main = Solution()

'''
def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return 
        root = TreeNode(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:nums.index(max(nums))])
        root.right = self.constructMaximumBinaryTree(nums[nums.index(max(nums))+1:])
        return root

'''