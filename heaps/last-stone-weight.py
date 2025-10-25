import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        """
            understanding:
                given a array of stones where stones[i] is weight of the ith stone

                I'm supposed to play a game with the stones until there is only one stone left
                the game is get the heaviest two stones and combine them if they
                are the same weight they will get destroyed. if one is greater then the other
                one will be destroyed and the other ones weight will be substracted by the destroyed stones weight.

                approach:
                    use a heap to always have a order list from greatest to lowest

                    while the list is greater then the length of 1 we will pop the last two elements combine them and push back there results if its not zero.
        """

        stones_heap = []

        # heapify the list using the max heap approach
        for n in stones:
            heapq.heappush(stones_heap,-n)
        
        while len(stones_heap) > 1:

            # convert numbers back to what they were so we can substract them
            x = heapq.heappop(stones_heap) * -1
            y = heapq.heappop(stones_heap) * -1

            if x - y != 0:

                # substract x - y and get abs value 
                # so we don't have to check which number is greater
                res = abs(x - y)
                heapq.heappush(stones_heap, res * -1)

        # if the list is empty return 0 else return the last number and convert it back to original value
        return stones_heap.pop() * -1 if len(stones_heap) > 0 else 0
        

        