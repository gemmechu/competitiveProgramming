from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def dfs(root, curr):
            if root:
                if(root.left !=None):
                    if(root.left.val> curr ):
                        dfs(root.left,curr)
                if (root.right != None):
                    if(root.right.val< curr):
                        dfs(root.right, curr)
            return root
        root = TreeNode(preorder[0])
        for i in range(1,len(preorder)):
            if(preorder[i]<root.val):
                dfs(root,root.val).left=TreeNode(preorder[i])
            if(preorder[i]>root.val):
                dfs(root, root.val).right = TreeNode(preorder[i])
        return root

preorder=[8,3,1,6,9]
main=Solution()
print(main.bstFromPreorder(preorder).left.val)