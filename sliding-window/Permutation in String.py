class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        """
            understand:
                1. two string s1 and s2
                2. return true or false if s2 has the characters that s1 has as a substring in any order

            question:
                does it have to be a premutation?
                what if the order in s2 is the same as s1?


        """


        count1 = {}
        n = len(s2)
         
        for c in s1:
            count1[c] = count1.get(c, 0) + 1

        need = len(count1)

        for i in range(n):
            count2, cur = {}, 0
            for j in range(i, n):
                c = s2[j]
                count2[c] = count2.get(c, 0) + 1
                if count1.get(c, 0) < count2[c]:
                    break
                if count1.get(c, 0) == count2[c]:
                    cur += 1
                if cur == need:
                    return True
        return False
        