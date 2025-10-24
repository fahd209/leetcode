import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.test_scores = nums
        heapq.heapify(self.test_scores)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.test_scores, val)

        # making sure the heap doesn't go over the len of k
        while len(self.test_scores) > self.k:
            heapq.heappop(self.test_scores)
        
        # the first item will always be the kth largest element since we are maintaining a heap of length k
        return self.test_scores[0]