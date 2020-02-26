class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
def validateBST(root: Node):

    if root:
        if(root.right != None):
            if(root.val > root.right.val):
                return False
        if (root.left != None):
            if (root.val < root.left.val):
                return False
        if(validateBST(root.left) == False):
            return False
        if(validateBST(root.right) == False):
            return False
    return True
def preOrder(root: Node):
    if root:
        print(root.val)
        inOrder(root.left)
        inOrder(root.right)
def inOrder(root: Node):
    if root:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)
def postOrder(root: Node):
    if root:
        inOrder(root.left)
        inOrder(root.right)
        print(root.val)
#in OrderTraversal check
result = []
def validateBSTinOrder(root: Node):
    if root:
        validateBSTinOrder(root.left)
        result.append(root.val)
        validateBSTinOrder(root.right)
    return result

root= Node(4)
a= Node(7)
b= Node(3)
c= Node(5)
d= Node(2)
e = Node(8)
root.left = b
root.right = a
a.left = c
b.left = d
b.right =e
#print(validateBST(root))
result_inOrder = validateBSTinOrder(root)
preOrder(root)
print("--------------")
inOrder(root)
print("--------------")
postOrder(root)
