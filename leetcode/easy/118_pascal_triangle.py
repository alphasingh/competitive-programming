"""
https://leetcode.com/problems/pascals-triangle/
"""


class Solution:
    # 1 <= numRows <= 30
    @staticmethod
    def generate(numRows: int) -> [[int]]:
        generations = [[1], [1, 1]]  # base cases
        for row in range(2, numRows):
            last_generation = generations[-1]
            adjacent_sums = []
            for i in range(len(last_generation) - 1):
                adjacent_sum = last_generation[i] + last_generation[i + 1]
                adjacent_sums.append(adjacent_sum)
            new_generation = [1] + adjacent_sums + [1]
            generations.append(new_generation)
        return generations[:numRows]


assert Solution.generate(numRows=1) == [[1]]
assert Solution.generate(numRows=5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

"""
Approaches:
1. Can be solved by pre-computing the results as numRows is small
2. Can be solved by brute force on runtime since numRows is small
"""
