class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_nth_from_end(head: ListNode, n) -> ListNode:
    if n == 0:
        return head
    total = 0
    node = head
    while node:
        total+=1
        node = node.next
    if total < n:
        count = 1

    else:
        count = total -n +1
    node = head
    prev = None
    while node:
        count -=1
        if count ==0:
            if prev is  None:
                return head.next
            prev.next = node.next
            return head
        prev, node = node, node.next

def print_linked_list(node):
    while node:
        print(node.val)
        node = node.next

n1, n2, n3, n4, n5 = (ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5))

n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n5
head = n1
head = remove_nth_from_end(head,2)
print_linked_list(head)