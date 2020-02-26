from typing import List

from leetcodecontest4.IncreasingBST import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
        return dfs(root, 0, [])


