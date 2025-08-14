class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        """
        1. first find the valid row
        2. if there is not valid rows return false
        3. else loop do a binary search on the valid row
        4. return true or false weither the value was found
        """

        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        if top > bottom:
            return False

        row = (top + bottom) // 2
        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1
        return False
                

        