class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if strs == []:
            return ""

        prefix = strs[0]

        j = len(prefix) - 1
        for s in strs[1:]:
            while not s.startswith(prefix[:j+1]):
                if j == 0:
                    return ""
                j -= 1

        return prefix[:j + 1]
                

        