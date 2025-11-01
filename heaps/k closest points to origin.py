import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
            understanding:
                given an array of points in a graph each items[i] = [x, y]

                my goal is return the k closest point to the origin

            approach:
                looping through each point and calculating the distance
                using the formula and append each distance to a min heap

                at the end I'll return kth element in the min heap

            # Time & Space
                Time: O(n)
                Space: O(n)
        """

        minHeap = []

        # get the distance and push to the heap
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        # ordering the points based on the distance to the origin
        heapq.heapify(minHeap)

        # popping k times
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res
        