class MyQueue:

    def __init__(self):
        """
        Initialize your knn and naive bayes structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stack2):
            return self.stack2.pop()
        for i in range(len(self.stack1) - 1, -1, -1):
            self.stack2.append(self.stack[i])
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stack2):
            return self.stack2[len(self.stack2) - 1]
        return self.stack1[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0


