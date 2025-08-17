class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        k = bananas per hour
        there are n piles of bananas
        return the minimum k bananas koko has to eat in each hour before the gaurd come back

        approach:
            [3,6,7,11]
            max: 11
            min: 1
            hours: 1 + 2 + 2 + 3
            res: 6, 4

            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
                  r   l    
                     k
        """


        res = float('inf')
        l = 1
        r = max(piles) 

        while l <= r:
            k = (l + r) // 2
            cur_h = 0
            for n in piles:
                cur_h += math.ceil(n / k)
                if cur_h > h:
                    l = k + 1
                    break
            
            if cur_h <= h:
                r = k - 1
                res = min(res, k)

        return res
        