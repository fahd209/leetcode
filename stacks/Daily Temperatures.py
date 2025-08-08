class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        """
        understand:
        given an array temperatures return array answer where 
        answers[i] == distance between answers[i] and a element thats greater the answers[i]
        if there is not greater element then answers[i] then set to zero

        approach:

        [73,74,75,71,69,72,76,73]
                         i
        [1, 1, 0, 2, 1, 0, 0, 0]
        [(2, 75), (3, 71)]

        Time: O(n)
        Space: O(n)
        """

        stack = []
        n = len(temperatures)
        ans = [0] * n

        for i in range(n):
            while stack and temperatures[i] > stack[-1][1]:
                prev_indx, num = stack.pop()
                ans[prev_indx] = i - prev_indx  

            stack.append((i, temperatures[i]))

        return ans


        # brute force (10 minutes)
        """
        n = len(temperatures)
        ans = [0] * n
        for i in range(n):
            for j in range(i, n):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break
        return ans
        """