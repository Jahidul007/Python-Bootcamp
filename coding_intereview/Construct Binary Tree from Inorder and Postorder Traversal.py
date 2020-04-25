# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root = TreeNode(postorder[-1])
        indx = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:indx], postorder[:indx])
        root.right = self.buildTree(inorder[indx + 1:], postorder[indx:-1])
        return root


"""
if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])

"""
