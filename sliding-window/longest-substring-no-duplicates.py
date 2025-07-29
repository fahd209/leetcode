class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        understand:
            set: b     
            input: "abcabcbb"
                           i
                           j
            out: 3

        approach:
            1. iterate through a string and every char that unique to a set
            2. while I'm i'll check while the current character is in the set if it is the increment the left index
            3. I'll have a variable that will keep max_length every iteration I'll reset it by setting it equal to the max between it self and length of the charSet
        """

        charSet = set()
        j = 0
        max_length = 0
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[j])
                j += 1
            charSet.add(s[i])
            max_length = max(len(charSet), max_length)


        return max_length