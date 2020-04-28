import heapq
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        nodes = []
        for l in lists:
            while(l):
                nodes.append(l)
                l = l.next

        if(len(nodes) == 0):
            return None
        nodes = sorted(nodes, key=lambda x: x.val)

        s = nodes[0]

        for n in nodes[1:]:
            s.next = n
            s = s.next

        return nodes[0]
if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list2 = ListNode(2)
    list2.next = ListNode(4)

    print(Solution().mergeKLists([list1, list2]))