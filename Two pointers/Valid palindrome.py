import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        understanding: 
            1. I'm given a string
            2. I have to return true or false if reads the same forwards and backwards with 
            all lower case letter, no spaces, no special characters

        approach:
            1. turn all letter lower case, remove special characters, and spaces
            2. set two pointer one in the start and one at the end
            3. set a while loop the will decrement the end pointer and increment the end pointer
            4. I'll check if the start pointer char is the same as the end pointer if not return false
            5. if the two pointers cross stop the loop and return true
        """

        clean_s = re.sub(r"[^a-zA-Z0-9 ]", '', s).replace(" ", '').lower()
        i = 0
        j = len(clean_s) - 1
        
        while i <= j:
            if clean_s[i] != clean_s[j]:
                return False
            
            i += 1
            j -= 1

        return True
        