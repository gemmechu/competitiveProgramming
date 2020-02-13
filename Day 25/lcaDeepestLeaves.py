# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def getheight(self,root: TreeNode) -> int:

        if root == None:
            return 0
        else:
            lHeight = self.getheight(root.left)
            RHeight = self.getheight(root.right)
            return max(lHeight,RHeight)+1


    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if root ==None:
            return None
        if(self.getheight(root.left)==self.getheight(root.right)):
            return root
        elif (self.getheight(root.left) > self.getheight(root.right)):
            return self.lcaDeepestLeaves(root.left)
        else:
            return self.lcaDeepestLeaves(root.right)

main=Solution()
root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(5)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(6)
root.left = a
a.left = b
root.right = c
c.right=d
d.right=e



print(main.lcaDeepestLeaves(root).val)