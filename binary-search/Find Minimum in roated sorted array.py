class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
            understanding:
                input: [3,4,5,1,2]
                output: 1
            
            requirements:
                1. must solve in O(log n)
                2. must return the minimum element in the array

            res: 5, 1, 
            approach:
                [3,4,5,1,2]
                         r
                         l
                         m

                res: 7, 1, 9
                [4,5,6,7,0,1,2]
                         l
                         r     m 

                [5,1,2,3,4]
                 l   m   r
        """


        l = 0
        r = len(nums) - 1
        result = float('inf')
        while l <= r:
            m = (l + r) // 2
            result = min(result, nums[m])

            if nums[m] >= nums[l]:
                if nums[m] < nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                 r = m - 1

        return result