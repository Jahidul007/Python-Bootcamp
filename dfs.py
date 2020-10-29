class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorderPrint(root):
    if root:
        inorderPrint(root.left)
        print(root.val)
        inorderPrint(root.right)
def preorderPrint(root):
    if root:
        print(root.val)
        preorderPrint(root.left)
        preorderPrint(root.right)
def postorderPrint(root):
    if root:
        postorderPrint(root.left)
        postorderPrint(root.right)
        print(root.val)



# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("\nInorder traversal of binary tree is")
inorderPrint(root)
print("\npreorder traversal of binary tree is")
preorderPrint(root)
print("\npostorder traversal of binary tree is")
postorderPrint(root)