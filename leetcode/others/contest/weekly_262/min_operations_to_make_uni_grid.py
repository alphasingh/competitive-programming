"""
https://leetcode.com/contest/weekly-contest-262/problems/minimum-operations-to-make-a-uni-value-grid/
"""


class Solution:
    @staticmethod
    def minOperations(grid: [[int]], x: int) -> int:
        min_operations = 0
        array = []
        for row in grid:
            array += row
        # print(array)
        array.sort()
        starter = array[0]
        for num in array:
            gap = num - starter
            min_operations += gap
            if gap % x != 0:
                return -1
        # print(min_operations)
        left = 0
        right = len(array)
        # print(array, left, right)
        current_operations = min_operations
        for i in range(1, len(array)):
            left += 1
            right -= 1
            difference = array[i] - array[i - 1]
            delta = (right - left) * difference
            # print(delta, difference)
            current_operations -= delta
            # print(current_operations)
            min_operations = min(min_operations, current_operations)
        # print(current_operations, min_operations)
        return min_operations // x


assert Solution.minOperations(grid=[[2, 4], [6, 8]], x=1) == 8
assert Solution.minOperations(grid=[[2, 4], [6, 8]], x=2) == 4
"""
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.
"""

assert Solution.minOperations(grid=[[1, 5], [2, 3]], x=1) == 5
"""
Explanation: We can make every element equal to 3.
"""

assert Solution.minOperations(grid=[[1, 2], [3, 4]], x=2) == -1
"""
Explanation: It is impossible to make every element equal.
"""
