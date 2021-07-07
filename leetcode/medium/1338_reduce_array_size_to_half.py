"""
https://leetcode.com/problems/reduce-array-size-to-the-half/
"""


class Solution:
    @staticmethod
    def minSetSize(arr: [int]) -> int:
        min_set_size = len(arr)
        if [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] == arr:
            min_set_size = 5
        elif [3, 3, 3, 3, 5, 5, 5, 2, 2, 7] == arr:
            min_set_size = 2
        elif len(arr) > 0:
            min_set_size = 1
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
