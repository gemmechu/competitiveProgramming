# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def inOrder(self,root:TreeNode,result):

        if root != None:
            self.inOrder(root.left,result)
            result.append(root.val)
            self.inOrder(root.right,result)
        return result

    def increasingBST(self, root: TreeNode) -> TreeNode:
        if(root ==None):
            return None
        inorderResult =(self.inOrder(root,[]))
        if(len(inorderResult)<=0):
            return None
        returnRoot= TreeNode(inorderResult[0])
        current = returnRoot
        for i in range(1,len(inorderResult)):
            current.right=(TreeNode(inorderResult[i]))
            current=current.right

        return returnRoot



def inOrder(root:TreeNode):

    if root != None:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)


root=TreeNode(5)
a=TreeNode(3)
b=TreeNode(6)
c=TreeNode(2)
d=TreeNode(4)
e=TreeNode(8)
f=TreeNode(1)
g=TreeNode(9)
h=TreeNode(7)
root.left=a
root.right=b
a.left=c
c.left=f
a.right=d
b.right=e
e.right=g
e.left=h

cc= TreeNode(23)
main=Solution()
solv=(main.increasingBST((root)))
inOrder(solv)