import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def isValidateBST(self, root:TreeNode) -> bool:
        def dfs(root:TreeNode, min:int,max:int):
            if not root:
                return True
            if(root.val<=min or root.val>=max):
                return False
            return dfs(root.left,min,root.val) and dfs(root.right,root.val,max)
        return dfs(root,sys.maxsize,-sys.maxsize)
main=Solution()

root=TreeNode(10)
a=TreeNode(5)
b=TreeNode(15)
c=TreeNode(6)
d=TreeNode(20)
root.left=a
root.right=b
b.left=c
b.right=d




print(main.isValidateBST(root))
