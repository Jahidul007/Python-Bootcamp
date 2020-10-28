# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 
        queue = [root]
        count = 0
        while queue:
            new_queue = []
            for index in queue:
                if index.left: 
                    new_queue.append(index.left)
                if index.right:
                    new_queue.append(index.right)
                count +=1
                    
            queue = new_queue
        return count
        
