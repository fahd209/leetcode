class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            understand:
                given an array return all combos the sum to the target
                1. you can use the same number twice
                2. all combinations must have a different frequency for each number
            
            approach:
                1. 
        """



        return self._combinationSum(candidates, target, 0)
    
    def _combinationSum(self, candidates, target, start_indx):
        if target == 0:
            return [[]]
        
        if target < 0:
            return []

        current_list = []
        for i in range(start_indx, len(candidates)):
            num = candidates[i]
            for comb in self._combinationSum(candidates, target - num, i):
                current_list.append([num] + comb)
        return current_list
        