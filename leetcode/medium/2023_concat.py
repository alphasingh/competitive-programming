"""
https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/
"""


class Solution:
    @staticmethod
    def numOfPairs(nums: [str], target: str) -> int:
        n = len(nums)
        valid = 0
        for i in range(n):
            for j in range(n):
                if i != j and target == nums[i] + nums[j]:
                    valid += 1
        return valid


assert Solution.numOfPairs(nums=["777", "7", "77", "77"], target="7777") == 4
"""
Explanation: Valid pairs are:
- (0, 1): "777" + "7"
- (1, 0): "7" + "777"
- (2, 3): "77" + "77"
- (3, 2): "77" + "77"
"""
assert Solution.numOfPairs(nums=["123", "4", "12", "34"], target="1234") == 2
"""
Explanation: Valid pairs are:
- (0, 1): "123" + "4"
- (2, 3): "12" + "34"
"""
assert Solution.numOfPairs(nums=["1", "1", "1"], target="11") == 6
"""
Explanation: Valid pairs are:
- (0, 1): "1" + "1"
- (1, 0): "1" + "1"
- (0, 2): "1" + "1"
- (2, 0): "1" + "1"
- (1, 2): "1" + "1"
- (2, 1): "1" + "1"
"""
