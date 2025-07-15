class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        [2,7,11,15], t = 9, out: [0, 1]

        will I get an empty array? and a target?

        approach:
        1. loop through the array substract the target - array[i] check if the result is in the hash map
        2. if yes return the indice of the item in the hashmap and then item of the array i

        time: o(n)
        space: o(n)
        """

        previous = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in previous:
                return [previous[comp], i]
            else:
                previous[nums[i]] = i