class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
            understanding:
                given array thats not sorted and im supposed to return the kth largest element

            approach:
                I'll loop of the nums arr and
                push each item to the max heap

                then I'll pop k times from the 
                heap
        """

        res = None
        maxHeap = []

        for n in nums:
            heapq.heappush(maxHeap, -n)

        while k > 0:
            res = heapq.heappop(maxHeap) * -1
            k -= 1

        return res