# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        q = [root]
        lis = []
        i =0
        while q:
            l = [node.val for node in q]
            lis.append(l)
            if len(lis)%2 ==0:
                lis[-1].reverse()
            q = [child for node in q for child in (node.left, node.right) if child]
        
        return lis
