# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        newhead = None

        while head:
            nextNode = head.next
            head.next = newhead
            newhead = head
            head = nextNode
        return newhead

print(Solution().reverseList([1,2,3,4,5]))