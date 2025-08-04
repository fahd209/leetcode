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

        result = []
        matching_parens = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for c in s:
            if c in matching_parens and result == []:
                return False

            if not c in matching_parens:
                result.append(c)

            if c in matching_parens:
                if result[-1] in matching_parens:
                    result.pop()

                if not result[-1] in matching_parens:
                    if matching_parens[c] == result[-1]:
                        result.pop()
                    else:
                        return False 


            

        return True if result == [] else False