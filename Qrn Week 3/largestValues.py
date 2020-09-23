# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root, level, result):
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
        result2 = []
        for item in result:
            result2.append(max(item))
        return result2
            
