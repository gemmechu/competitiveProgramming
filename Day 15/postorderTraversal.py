from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root : TreeNode, result: List[int]):
            if root:
                if(root.left != None):
                    dfs(root.left, result)
                if(root.right != None):
                    dfs(root.right, result)
                result.append(root.val)
            return result
        return dfs(root, [])
root= TreeNode(1)
a= TreeNode(2)
b= TreeNode(3)
root.right = a
a.left = b
main = Solution()
print(main.postorderTraversal(root))