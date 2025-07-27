class Solution:
    def trap(self, height: List[int]) -> int:

        """
        Time: o(n)
        space: o(n)
        """

        n = len(height)
        max_left = 0
        max_right = 0
        left_max_values = [0] * n
        right_max_values = [0] * n
        res = 0

        for i in range(n):
            left_max_values[i] = max_left
            if i == 0:
                left_max_values[i] = 0
            max_left = max(max_left, height[i])
        
        for i in range(n - 1, -1, -1):
            right_max_values[i] = max_right
            if i == n - 1:
                right_max_values[i] = 0
            max_right = max(max_right, height[i])

        for i in range(n):
            water_amount = min(left_max_values[i], right_max_values[i]) - height[i]
            if water_amount >= 0:
                res += water_amount
        
        return res