# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(root, result, cnt):
            if root:
                if root.left == None and root.right == None:
                    result.append(cnt)
                    return result 
                dfs(root.left, result, cnt+1)

                dfs(root.right, result, cnt+1)
            
            return result
        result = dfs(root, [], 1)
        print(result)
        
        
        return min(result)
            
