class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode) -> ListNode:
        value = 0
        currentNode = head
        while currentNode!=None :
            node = currentNode
            while node.next!=None:
                if node.next.value == currentNode.value:
                    node.next = node.next.next
                else:node = node.next

            currentNode = currentNode.next
        return head





