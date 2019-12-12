class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
def searchBST(root:TreeNode,val:int)->TreeNode:
        if root and val < root.val:
            return searchBST(root.left, val)

        if root and val > root.val:
            return searchBST(root.right, val)
        
        return root
def printPreoder(root:TreeNode):
    if root:
        print (root.val)
        printPreoder(root.left)
        printPreoder(root.right)
root= TreeNode(1)
a=TreeNode(2)
b=TreeNode(10)
c=TreeNode(5)
d=TreeNode(7)
root.right=a
a.left=b
b.right=c
c.left=d
root1= searchBST(root,2)
printPreoder(root1)