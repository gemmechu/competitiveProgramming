class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def isValidateBST(self, root:TreeNode) -> bool:
        if(not root):
            return False
        def dfs(root: TreeNode, preRoot:TreeNode, direction:str):
            if root:
                if(direction=="left"):
                    if(not(root.val <preRoot.val)): #1<2
                      return False
                if (direction == "right"):
                    if (not (root.val > preRoot.val)): #3>2
                        return False

                if(dfs(root.left,root,"left")==False):
                    return False


                if(dfs(root.right, root, "right")==False): #3,2,right
                    return False
            return True

        return dfs(root,None,"")
main=Solution()

root=TreeNode(3)
a=TreeNode(2)
b=TreeNode(1)
root.left=a
a.left=b


c=TreeNode(2)
d=TreeNode(4)
e=TreeNode(8)
f=TreeNode(1)
g=TreeNode(9)
h=TreeNode(7)


print(main.isValidateBST(root))
