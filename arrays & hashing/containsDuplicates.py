class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        [1,2,3,1] -> true
        return true or false if it contains duplictes

        empty list -> false 

        approach:
            1. inslize a set
            2. loop through the array
            3. check if the element is in the set 
            4. if the element is in the set return true else keep going
            5. if i loop through the whole array and there is duplicates return False

        """

        duplicates = set()

        for n in nums:
            if n in duplicates:
                return True
            else:
                duplicates.add(n) 
        return False