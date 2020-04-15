class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count = 1
        root = ListNode(0)
        root.next = head
        pre = root
        while pre.next and count < m:
            pre = pre.next
            count += 1
        if count < m:
            return head
        mNode = pre.next
        curr = mNode.next
        while curr and count < n:
            next = curr.next
            curr.next = pre.next
            pre.next = curr
            mNode.next = next
            curr = next
            count += 1
        return root.next