# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if head.next is None:
            return None
        if head.next.next is None:
            return None

        slow, fast = head, head

        slow = head.next
        fast = fast.next.next

        while slow != fast:
            slow = slow.next
            if slow is None:
                return None
            if fast.next is None:
                return None
            fast = fast.next.next
            if fast is None:
                return None

            node = head
            while node != slow:
                node = node.next
                slow = slow.next
            return node
