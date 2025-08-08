class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        I'm given n number of parenthese
        return all valid combination of those parentheses. 
        each parentheses bracket should be closed by another parentheses bracket

        approach:
            n = 3
                    [(]
                [()]    ["(("]


        """

        result = []
        self.generate(result, [], n, 0, 0)
        return result

    def generate(self, result, currentComb, n, open_count, close_count):
        if open_count == close_count == n:
            result.append(''.join(currentComb))
            return


        if open_count < n:
            self.generate(result, currentComb + ["("], n, open_count + 1, close_count)

        if close_count < open_count:
            self.generate(result, currentComb + [")"], n, open_count, close_count + 1)
        
        
        