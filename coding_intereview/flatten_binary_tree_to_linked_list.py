# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root

        list = []

        def preorder(node):
            if node is None:
                return
            list.append(node)
            preorder(node.left)
            preorder(node.right)
        preorder(root)

        list.append(None)

        for i, item in enumerate(list):
            if item is None:
                break
            item.left = None
            item.right = list[i+1]
        return list[0]