class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
            understand: 
                1. given an array nums
                2. return an array of the whole arrays product. except nums[i]
            
            example:
            input:   [1, 2, 3, 5]
            output:    [30, 15, 10, 6]

            approach:
                1. get prefix of the whole array where prefix[i] is the product of the whole array except it self
                2. get the suffix of the whole array where suffix[i] is the product of the whole array except it self
                3. then I'll multiply the suffix and prefix

            prefix: [1, 1, 2, 6]
            suffix: [30, 15, 5, 1]
            output: [30, 15, 10, 6]
        """

        n = len(nums)
        prefix = []
        suffix = [1] * n
        result = [0] * n

        product_one = 1
        for i in nums:
            prefix.append(product_one)
            product_one *= i

        product_two = 1
        for i in range(n - 1, -1, -1):
            suffix[i] = product_two
            product_two *=  nums[i]

        print(prefix)
        print(suffix)

        for i in range(n):
            result[i] = prefix[i] * suffix[i] 

        return result

        