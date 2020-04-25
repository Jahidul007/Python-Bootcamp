# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node):
            if node == None:
                return 0
            return max(height(node.left), height(node.right)) + 1

        if root == None:
            return 1
        leftBalanced = self.isBalanced(root.left)
        rightBalanced = self.isBalanced(root.right)

        leftHeight = height(root.left)
        rightHeight = height(root.right)

        return 1 if abs(leftHeight - rightHeight) <= 1 and leftBalanced and rightBalanced else 0
