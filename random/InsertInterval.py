class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        []
        [[1,5],[2,5],[6,9]]

        approach:
            1. fist intert the new interval
            2. sort in acending order
            3. check for overlapped elements and merge them so that there is not overlapped elements example:
                1. [[1,5],[6,9]]
                2. 

            Time: o(n log(n))
        """
        intervals.append(newInterval)
        combined_intervals = sorted(intervals, key=lambda x: x[0])
        result_array = []

        current_element = combined_intervals[0]
        for interval in combined_intervals[1:]:
            a, b = interval
            if current_element[1] >= a:
                if current_element[1] <= b:
                    current_element[1] = b
            else:
                result_array.append(current_element)
                current_element = interval
        result_array.append(current_element)


        return result_array
        
