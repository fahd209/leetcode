class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
            understanding:
                1. input array heights where height[i] represented the height of a line on the index i
                2. I need to find two points that contain the most water

                 0 1 2 3 4 5 6 7 8 9
                [1,8,6,2,5,4,8,3,7,9]
                     l             r

                max_height = 9, 64, 
                1. (9 - 0) = 9 * min(1, 8) = 9
                2. (9 - 1) = 8 * min(8, 9) =  64
                3. (9 - 2) = 7 * min(9, 6) = 
            approach:42
                1. two pointers 1 at the begining one at the end
                2. 
        """

        res = 0
        i = 0
        j = len(height) - 1
        while i < j:
            amount_of_water = (j - i) * min(height[i], height[j])
            res = max(res, amount_of_water)
            if height[i] > height[j]:
                j -= 1
            elif height[i] < height[j]:
                i += 1
            else:
                i += 1
                j -= 1

        return res