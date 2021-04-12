"""
https://leetcode.com/problems/beautiful-arrangement-ii/
"""


class Solution:
    @staticmethod
    def constructArray(n: int, k: int) -> [int]:
        remaining = [i for i in range(1, n + 1)][k + 1:]
        current = 1  # start with 1
        sign = 1  # start with positive
        beautiful = [current]  # start with 1
        while k > 0:
            current += k * sign
            beautiful.append(current)
            k -= 1  # decrease k
            sign = -sign  # switch sign
            # print(k, sign)
        # print(beautiful)
        beautiful += remaining
        # print(beautiful)
        return beautiful


assert Solution.constructArray(n=8, k=1) == [1, 2, 3, 4, 5, 6, 7, 8]
assert Solution.constructArray(n=8, k=2) == [1, 3, 2, 4, 5, 6, 7, 8]
assert Solution.constructArray(n=8, k=3) == [1, 4, 2, 3, 5, 6, 7, 8]
assert Solution.constructArray(n=8, k=4) == [1, 5, 2, 4, 3, 6, 7, 8]
assert Solution.constructArray(n=8, k=5) == [1, 6, 2, 5, 3, 4, 7, 8]
assert Solution.constructArray(n=8, k=6) == [1, 7, 2, 6, 3, 5, 4, 8]
assert Solution.constructArray(n=8, k=7) == [1, 8, 2, 7, 3, 6, 4, 5]
"""
Use whiteboard test cases that helped build the algorithm with n=8 and all possible k=1 to k=7 values
"""
assert Solution.constructArray(n=3, k=1) == [1, 2, 3]
"""
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, 
and the [1, 1] has exactly 1 distinct integer: 1.
"""
assert Solution.constructArray(n=3, k=2) == [1, 3, 2]
"""
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, 
and the [2, 1] has exactly 2 distinct integers: 1 and 2.
"""
