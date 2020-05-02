class MinStack:

    def __init__(self):
        """
        initialize your knn and naive bayes structure here.
        """
        self.stk = []
        self.min_stk = []

    def push(self, x: int) -> None:
        self.stk.append(x)
        if len(self.min_stk)== 0 or x <= self.min_stk[-1]:
            self.min_stk.append(x)
            print(self.min_stk[-1])
            print(self.min_stk)

    def pop(self) -> None:
        x = self.stk.pop()
        if x == self.min_stk[-1]:
            self.min_stk.pop()

    def top(self) -> int:
        if len(self.stk) != 0:
            return self.stk[-1]

    def getMin(self) -> int:
        if len(self.min_stk) != 0:
            return self.min_stk[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


ls = [1,2,3,4,5,6,7,8]
print(ls[-1])