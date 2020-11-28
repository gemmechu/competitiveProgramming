# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(left:TreeNode,right:TreeNode):
            if left == None or right ==None:
                return left == right
            
            if left.val != right.val:
                return False
            
            
            return isMirror(left.left,right.right) and isMirror(left.right, right.left)
        if root == None:
            return True
        return isMirror(root.left, root.right)
