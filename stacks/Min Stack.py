import heapq
class MinStack:

    """
    # Approach
    For this problem I used two stack, one to maintain the operations and one to maintain the min value. 
    I maintained the minValue by comparing the value that's being pushed to the last value in the minStack.
    if the value being push is less then the last value in the stack then I'll append the current value to
     the top of the stack if not the value that's being pushed will be the same as the previous one in the minStack.
    """

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        if self.stack != []:
            return self.stack[-1]

    def getMin(self) -> int:

        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()