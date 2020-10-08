# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        if root == None:
            return res
        q = [root]
        print(q)
        while q:
            l = [node.val for node in q]
            print (l)
            res.append(sum(l)/len(l))
            q = [child for node in q for child in (node.left, node.right) if child]
        return res
