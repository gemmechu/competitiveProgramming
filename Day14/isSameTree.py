class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def isSameTree(self,p: TreeNode, q:TreeNode)->bool:
        

        if p and q:
            print(str(p.val)+' '+str(q.val))
            if(p.val==q.val):
                result = self.isSameTree(q.left,p.left)
                if(result==False):
                    return result
                result= self.isSameTree(q.right,p.right)
                if(result==False):
                    return result
        

            if(p.val != q.val):
                result= False
                return result
        else:
            if(p==None and q!=None):
                print(str(p)+' '+str(q.val))
                result=False
                return result
            if(p!=None and q==None):
                print(str(p.val)+' '+str(q))
                result=False
                return result
        
        return True
def printPreoder(root:TreeNode):
    if root:
        print (root.val)
        printPreoder(root.left)
        printPreoder(root.right)
    

root= TreeNode(1)
root1=TreeNode(1)

a=TreeNode(2)
b=TreeNode(10)
c=TreeNode(5)
d=TreeNode(7)

root1.right=b
root.right=b
b.right=c
c.left=d




sol= Solution()
print(sol.isSameTree(root,root1))

printPreoder(root)       
printPreoder(root1)       

