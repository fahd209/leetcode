class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """

        understand: Given an input array return all 3 number combination that sums up to 0 in a 2d list. 
        you cannot resuse any of the same numbers twice for the sum even if it somes to 0. 

        [[-1,-1,2], [-1, 0, 1]]
        [-1,0,1,2,-1,-4]
        [-4,-1,-1,0,1,2]
             i    l r

        [-1,-1,1,0]
         i     l r
        """

        result = []
        nums.sort()
        print(nums)

        
        for i in range(len(nums)):
           

            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result