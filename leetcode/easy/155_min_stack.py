"""
https://leetcode.com/problems/min-stack/
"""


class MinStack:

    def __init__(self):
        self.minimum = 2147483648
        self.top_element = 0
        self.stack = [None]
        self.minimum_history = [2147483648]
        # print(self.minimum, self.top_element, self.stack, self.minimum_history)

    def push(self, val: int) -> None:
        # print('pushing: ', val)
        self.stack.append(val)
        # update minimum
        self.minimum = min(self.minimum, val)
        self.minimum_history.append(self.minimum)
        self.top_element = val
        # print(self.minimum, self.top_element, self.stack, self.minimum_history)

    def pop(self) -> None:
        # print('pop')
        self.stack.pop()
        self.minimum_history.pop()
        self.minimum = self.minimum_history[-1]
        self.top_element = self.stack[-1]
        # print(self.minimum, self.top_element, self.stack, self.minimum_history)

    def top(self) -> int:
        # print('top')
        # print(self.minimum, self.top_element, self.stack, self.minimum_history)
        return self.top_element

    def getMin(self) -> int:
        # print('min')
        # print(self.minimum, self.top_element, self.stack, self.minimum_history)
        return self.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
assert minStack.getMin() == -3
minStack.pop()
assert minStack.top() == 0
assert minStack.getMin() == -2
"""
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
"""
