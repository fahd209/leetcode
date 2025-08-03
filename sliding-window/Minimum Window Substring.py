class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        understand:
            I'm given a string s and t, I have to return a substring of s where all t's characters are included, even if t's characters have to duplicates
            the string has to have duplicates. If I can't find substring that has all of t's characters then I should return ""

        approach:
            res: 0
            {
                "ADOBEC": 6,

            }
            {
                "A": 1
                "B": 1
                "C": 1
            }
            {
                "A": 1
                "B": 1
                "C": 1
            }
            need: 3 
            cur: 3
            res: 0, 5
            res: 8, 11
            "ADOBECODEBANC"
                          i 
                       j

        """

        count1 = {}
        count2 = {}
        for c in t:
            count1[c] = count1.get(c, 0) + 1
            count2[c] = 0

        res, resLen = [-1, -1], float('infinity')
        need = len(count1)
        l = 0
        cur = 0

        for r in range(len(s)):
            if s[r] in count1:
                count2[s[r]] += 1

            if s[r] in count1 and count1[s[r]] == count2[s[r]]:
                cur += 1
            print(cur)
            while need == cur:
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = [l, r]
                
                if s[l] in count2:
                    count2[s[l]] -= 1
                    if count2[s[l]] < count1[s[l]]:
                        cur -= 1
                

                l += 1

        l, r = res
        return s[l: r + 1] if resLen != float('infinity') else ""