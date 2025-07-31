
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            understand: 
            i'm given a string s i can change the character of the string k amount of times, 
            i have to return the longest substring containing the same characters after changing them

            approach:
                count: 
                {
                    A: 2
                    B: 3
                }
                res: 0, 1, 2, 3, 4
                current: AABABBA
                           l
                                r
        """

        max_length = 0
        charCount = {}
        l = 0
        maxf = 0
        for r in range(len(s)):
            window_length = (r - l + 1)
            c = s[r]
            charCount[c] = charCount.get(c, 0) + 1
            maxf = max(maxf, charCount[c])
            replacements = window_length - maxf

            while (r - l + 1) - maxf > k:
                charCount[s[l]] -= 1
                l += 1
                maxf = max(maxf, charCount[c])

            max_length = max(max_length, (r - l + 1))



        return max_length
        