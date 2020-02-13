# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if root !=None:
            if (root.left == None and root.right == None):
                if (sum == root.val):

                    return True

            if(self.hasPathSum(root.left,sum-root.val)):
                return True

            if(self.hasPathSum(root.right,sum-root.val)):
                return True
        return False


if __name__ == '__main__':
    main= Solution()
    root = TreeNode(5)
    a = TreeNode(4)
    b = TreeNode(8)
    c = TreeNode(11)
    d = TreeNode(13)
    root.left=a
    root.right=b
    a.left=c
    b.left=d
    sum=21
    print(main.hasPathSum(None,sum))


