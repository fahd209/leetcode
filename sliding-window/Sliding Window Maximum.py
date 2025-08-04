class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        understand:
            1. given an array numbers and k window size
            2. the window will always size k and will be moving by one position in each iteration
            3. return array of the max values in each window

        approach:
        [1,3,-1,-3,5,3,6,7] k = 3
                       i
                           j 
              
        [7]
        [3, 3, 5, 5, 6, 7]
         
        """

        output = []
        queue = deque()
        l, r = 0, 0

        while r < len(nums):
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            queue.append(r)

            if (r - l) + 1 == k:
                output.append(nums[queue[0]])
                l += 1
            
            if l > queue[0]:
                queue.popleft()

            r += 1
            

        return output
