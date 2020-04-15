class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteMiddleNode(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return None

    prev, slow, fast = None, head, head
    """
    middle-of-the-linked-list
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        return slow

    """

    while fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next

    return head


def print_linked_list(node):
    while node:
        print(node.val)
        node = node.next


n1, n2, n3, n4, n5 = (ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5))

n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n5
head = n1
head = deleteMiddleNode(head)
print_linked_list(head)



