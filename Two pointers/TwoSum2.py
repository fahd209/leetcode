class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        understand:
            1. input a numbers array: [2,3,4] starting index is 1 not 0
            2. return two numbers index 1 and index 2
            3. output-rules:
                1. numbers[index1] + numbers[index2] = target
                2. index 1 >= 1
                3. index2 > index1 and <= len(numbers)
        
        target: 9
        1. 2 + 15 = 17 > target
        2. 2 + 11 = 13 > target
        3. 2 + 7 = target return [1, 2]
        approach: [2,7,11,15]
                   i j

        Time: o(n)
        space: o(1)
        """

        i = 0
        j = len(numbers) - 1

        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i + 1, j + 1]
            if sum > target:
                j -= 1
            else:
                i += 1
        


