class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
def trim(root: Node, min: int, max: int):
    if root:
        root.left = trim(root.left,min, max)
        root.right = trim(root.right ,min, max)

        if(min <= root.val <= max):
            return  root
        if(root.val < min):
            return root.right
        if root.val > max:
            return root.left

    return root
def inOrder(root: Node):
    if root:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)

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
result = trim(root, 3, 7)
inOrder(result)

