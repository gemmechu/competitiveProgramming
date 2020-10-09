# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        def dfs(root, result, level):
            if  root:
                if result.get(level) != None:
                    result[level].append(root.val)
                else:
                    result[level] = [root.val]
                dfs(root.left, result, level+1)
                
                dfs(root.right, result, level+1)
                
                
            return result
        reverse = dfs(root,{},0)
        reverse = (list(reverse.values()))
        result = []
        for i in range(len(reverse)):
            result.append(reverse[len(reverse)-i-1])
        return result
