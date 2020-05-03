# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        indx = 1
        p_len = len(preorder)
        while indx < p_len and preorder[0] > preorder[indx]:
            indx += 1
        root.left = self.bstFromPreorder(preorder[1:indx])
        root.right = self.bstFromPreorder(preorder[indx:])

        return root