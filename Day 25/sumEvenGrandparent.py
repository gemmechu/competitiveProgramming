# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    result = 0
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(root:TreeNode ,prnt : int,gpt: int)->int:
            if root:
                if gpt %2 ==0:
                    self.result+=root.val
                dfs(root.left,root.val,prnt)
                dfs(root.right, root.val, prnt)
            return self.result
        return dfs(root,1,1)
main=Solution()
root = TreeNode(8)
a = TreeNode(4)
b = TreeNode(8)
c = TreeNode(11)
d = TreeNode(13)
root.left = a
root.right = b
a.left = c
b.left = d

print(main.sumEvenGrandparent(root))
