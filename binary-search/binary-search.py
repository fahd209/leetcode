class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        understand:
            I'm given an array sorted from lowest to highest and a target integer. I have to
            search throught the array in o(log n) time if there target is in the array return the index
            if not return -1

        what if the array is empty or the array has only two elements or one element?


        approach:
              0 1 2 3 4 5
            [-1,0,3,5,9,12]
              l r
              m         
                 
        """

        l = 0
        r = len(nums) - 1

        if nums == []:
            return -1

        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            
            if nums[m] > target:
                r = m - 1
                
            if nums[m] < target:
                l = m + 1


        return -1


        
        