# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import numpy as np
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []
        def findpath(root,target, result, path):
            if not root:
                return
            path.append(root.val)    
            if(root.val == target and root.left == None and root.right == None):
                result.append(path)
            findpath(root.left, target-root.val, result, path.copy())
            findpath(root.right, target-root.val, result, path.copy())
            return result
        result = findpath(root, sum, result,[])
        return result
