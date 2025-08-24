class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        input: s: string, k: integer
        output: the longest substring with k letter replacement

        requirments:
            1. choose any character to change
            2. you may only change a character k times
        
        approach:
            "ABAB"
            k: 2
            {
                a: 2
                b: 2
            }
            max = 1, 2, 3, 4, 
            AABABBA
               l
                  r

            {
                a: 3
                b: 1
            }
            "AABABBA"
             r
                l

            Time: O(n)
            Space: O(n)
        """

        l = 0
        window = {}
        result = float('-inf')

        
        max_occured_c = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            max_occured_c = max(max_occured_c, window[s[r]])

            while (r - l + 1) - max_occured_c > k:
                window[s[l]] -= 1
                l += 1
            
            result = max(result, (r - l + 1))

        return result



        