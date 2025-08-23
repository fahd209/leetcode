class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            understanding:
                given a string find of n characters
                return the length of longest substring with repeating charactrers

                example:
                    input: "abcabcbb"
                    output: 3, why? because the longest substring with repeating characters is 'abc'

            approach:
                  set: c, a, b
                  max = 0, 1, 2, 3
                  "abcabcbb"
                     i 
                        j


            
        """

        if len(s) == 0:
            return 0

        charSet = set()
        i = 0
        j = 0
        max_substring = float('-inf')
        while i < len(s):
            while s[i] in charSet:
                charSet.remove(s[j])
                j += 1

            charSet.add(s[i])
            max_substring = max(len(charSet), max_substring)
            i += 1

        return max_substring

