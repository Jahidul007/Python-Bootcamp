# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        q = [root]
        lis = []
        i =0
        count = 0
        while q:
            l = [node.val for node in q]
            lis.append(l)
            
            q = [child for node in q for child in (node.left, node.right) if child]
        print(lis)
        lastNode = []
        for i in range(len(lis)):
            lastNode.append(lis[i][len(lis[i])-1])
        return lastNode
            
