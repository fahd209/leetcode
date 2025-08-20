class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        understand:
            given an input array nums
            return all possible possible sets the sum to 0
        
        requirments:
            1. no duplicate subsets
            2. i can NOT equal to j or k
            3. and j can NOT equal to k


        approach:
            1. sort the array. why: so we can use the two pointer pattern to increase or decrease the sum
            2. for each iteration of I I'll use the two pointer pattern to increase or decrease the sum
             [-1,0,1,2,-1,-4]
             [[-1, -1, 2], [-1, 0, 1]]
             [-4, -1, -1, 0 1, 2]
                            i
        """

        result = []
        nums.sort()

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            if nums[i] > 0:
                return result

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:         
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result