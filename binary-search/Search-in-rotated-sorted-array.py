class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """
            understanding:
                    proir to input: [0,1,2,4,5,6,7]
                    intput: [4,5,6,7,0,1,2]


                    output: indice of the target if target is not in the array return -1


            approach:
                k: 3
                i: 
                j:
                m: i + j - k
                target: 2
                [5,6,7,0,1,2,4]
                        l  m  r   
        """

        l, r = 0, len(nums) - 1

        while l <= r:
            print((l, r))
            m = (l + r) // 2 
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[r] >= target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1

        return -1 