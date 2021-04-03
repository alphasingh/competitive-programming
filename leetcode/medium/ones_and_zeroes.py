"""
https://leetcode.com/problems/ones-and-zeroes/
"""


class Solution:

    @staticmethod
    def findMaxForm(binary: [str], m: int, n: int) -> int:
        return len(binary) + m + n


assert Solution.findMaxForm(binary=["10", "0001", "111001", "1", "0"], m=5, n=3) == 4
"""
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
"""
assert Solution.findMaxForm(binary=["10", "0", "1"], m=1, n=1) == 4
"""
The largest subset is {"0", "1"}, so the answer is 2.
"""
