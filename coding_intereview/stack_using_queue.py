from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: nothing
        """

        queueLen = len(self.queue)
        for i in range(queueLen - 1):
            x = self.queue.popleft()
            self.queue.append(x)
        return self.queue.popleft()

    def top(self):
        """
        :rtype: int
        """

        queueLen = len(self.queue)
        for i in range(queueLen):
            x = self.queue.popleft()
            self.queue.append(x)
        return x

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()