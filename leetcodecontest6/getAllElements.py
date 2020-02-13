# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def getAllElement(root:TreeNode,mylist : List[int])-> List[int]:
            if root:
                getAllElement(root.left,mylist)
                mylist.append(root.val)
                getAllElement(root.right, mylist)
            return mylist

        root1list= getAllElement(root1,[])
        result = getAllElement(root2, root1list)
        return sorted(result)

main=Solution()

root=TreeNode(-5)
a=TreeNode(3)
b=TreeNode(6)


root.left=a
root.right=b

root2=TreeNode(10)
a2=TreeNode(1)
b2=TreeNode(6)


root2.left=a2
root2.right=b2


print(main.getAllElements(root,root2))
