class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
            understand: [1, 2, 3] -> return all combination of subsets all subsets have to be unique

            approach:
                1. inclusive and declusive pattern
                [2, 3]
             2    / \ 
                /    \
                3     3
           3  /\  3  / \
            []  []  []  []   


        [
            [[2,3], [2], [[3], []]]
   
        ]
        """
        if nums == []:
            return [[]]

        first = nums[0]
        inclusive = self.subsets(nums[1:])
        for item in inclusive:
            item.append(first)
        exclusive = self.subsets(nums[1:])
        return inclusive + exclusive