class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        understanding:
            input: [100,4,200,1,3,2]
            output: 4
            why: [1, 2, 3, 4]

        approach:
            max: 1, 2, 3, 4 
            set: 
            array: [100,4,200,1,3,2]
         iterator:            i


        """

        sequence_set = set(nums)
        max_seq = 0

        for n in sequence_set:
            if not n - 1 in sequence_set:
                cur = n 
                count = 1
                while cur + 1 in sequence_set:
                    count += 1
                    cur = cur + 1
                max_seq = max(max_seq, count)


        return max_seq

        