class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        understanding:
            given an array height return the max area of the array

        example:
            [2,1,5,6,2,3]
            output: 10

        approach:
            maxArea: 0, 2, 6, 10
            stack:    [(0,1), (2, 2), (5, 3)]
            array:    [2,1,5,6,2,3]
            indices:   0 1 2 3 4 5
            iterator:            i 

            stack: [(0,1)]
            maxArea: 10
        """

        stack = []
        maxArea = float('-inf')

        for i, n in enumerate(heights):
            cur = (i, n)
            while stack and n < stack[-1][1]:
                prev_indx, height = stack.pop()
                width = i - prev_indx
                maxArea = max(maxArea, width * height)
                cur = (prev_indx, n)

            stack.append(cur)


        while stack:
            index, height = stack.pop()
            width = len(heights) - index
            maxArea = max(maxArea, width * height)

        return maxArea
        