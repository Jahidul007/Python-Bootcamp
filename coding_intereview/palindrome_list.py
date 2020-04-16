# Definition for singly-linked list.
"""
** Using stack
        stk = []
        node = head

        while node:
            stk.append(node.val)
            node = node.next
            node = head
            while node:
                if node.val != stk[-1]:
                    return False
                node = node.next
                stk.pop()
            return True
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # without extra memory
        count = 0
        node = head
        while node:
            count += 1
            node = node.next

        # reverse first half list
        prev, node = None, head

        for _ in range(count / 2):
            temp_node, node.next = node.next, prev
            prev, node = node, temp_node

        if count % 2 == 1:
            node = node.next
        while node:
            if node.val != prev.val:
                return False
            node, prev = node.next, prev.next
        return True
