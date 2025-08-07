class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        """
        understand:
            given the following array of string which contain numbers and operations. 
            if there is a operation after two numbers then the operation with performed to 
            those two numbers.
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

        approach:
            1. iterate throught the string if c is at a number convert it to a num and append to the stack
            2. if c is at operation then pop the two last items in the stack and perform the operation
            3. the order in which we do the operation the last two numbers only matters if the operation
                is a "-" or "/"

        """
        

        stack = []
        for c in tokens:
            if c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(math.trunc(b / a))
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(c))

        return stack[-1]
        