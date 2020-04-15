class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        head, prev = None, None

        current_old, current = None, head

        while current:
            current_old = current
            while current.next and current.val == current.next.val:
                current = current.next
            if current_old == current:
                if head is None:
                    head = current_old
                else:
                    prev.next = current_old
                    current = current.next
                    prev = current_old
                    prev.next = None
            else:
                current = current.next

        return head