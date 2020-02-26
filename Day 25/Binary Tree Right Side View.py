# Definition for a binary tree node.
from typing import List


class TreeNode:
 def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def dfs(root: TreeNode, level: int, result: List[int]):
            if not root:
                return
            if len(result) < level + 1:
                result.append([])
            result[level].append(root.val)
            dfs(root.left, level+1, result)
            dfs(root.right, level + 1, result)
            return result
        if not root:
            return []
        result = dfs(root, 0, [])
        for j in range(len(result)):
            result[j] = result[j][-1]
        return result