class Solution:
    def isValid(self, s: str) -> bool:
        """
        understand:
        I'm given a string I'm supposed to return true or false if the string meets all these condition
        1. an open bracket has corresponding closing bracket
        2. brackets opening and closing must be in order

        approach:
            1. use a hash map to match closing brack with opening brackets
            "([])"
                 i
            ""
        """

        stack = []
        matching_parens = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for c in s:
            if c in matching_parens:
                if stack and stack[-1] == matching_parens[c]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(c)


            

        return True if not stack else False