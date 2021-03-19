"""
https://leetcode.com/problems/di-string-match/
"""


class Solution:
    @staticmethod
    def diStringMatch(string: str) -> [int]:
        string_length = len(string)
        d_counter = string_length
        i_counter = 0
        permutation = list()
        for index in range(string_length):
            if string[index] == "I":
                permutation.append(i_counter)
                i_counter += 1
            else:  # string[index] == "D"
                permutation.append(d_counter)
                d_counter -= 1
        permutation.append(i_counter)  # here i_counter == d_counter
        # print(permutation)
        return permutation


assert Solution.diStringMatch(string="IDID") == [0, 4, 1, 3, 2]
assert Solution.diStringMatch(string="III") == [0, 1, 2, 3]
assert Solution.diStringMatch(string="DDI") == [3, 2, 0, 1]

"""
Example 1:

Input: "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: "III"
Output: [0,1,2,3]
Example 3:

Input: "DDI"
Output: [3,2,0,1]
"""

"""
Note:
1 <= S.length <= 10000
S only contains characters "I" or "D".
"""
