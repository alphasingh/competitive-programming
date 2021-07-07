"""
https://leetcode.com/problems/reduce-array-size-to-the-half/
"""


class Solution:
    @staticmethod
    def minSetSize(arr: [int]) -> int:
        min_set_size = 0
        removed_array_size = 0
        required_half_size = len(arr) // 2
        frequencies = {}
        for element in arr:
            if element not in frequencies:
                frequencies[element] = 0
            frequencies[element] += 1
        # print(frequencies)
        for frequency in sorted(frequencies.values(), reverse=True):
            if removed_array_size < required_half_size:
                min_set_size += 1
                removed_array_size += frequency
            else:
                break
        # print(min_set_size)
        return min_set_size


assert Solution.minSetSize(arr=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7]) == 2
"""
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] 
which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] 
which has size greater than half of the size of the old array.
"""

assert Solution.minSetSize(arr=[7, 7, 7, 7, 7, 7]) == 1
"""
Explanation: The only possible set you can choose is {7}. This will make the new array empty.
"""

assert Solution.minSetSize(arr=[1, 9]) == 1
assert Solution.minSetSize(arr=[1000, 1000, 3, 7]) == 1
assert Solution.minSetSize(arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
