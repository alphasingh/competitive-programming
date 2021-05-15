"""
https://leetcode.com/problems/jewels-and-stones/
"""


class Solution:
    @staticmethod
    def numJewelsInStones(jewels: str, stones: str) -> int:
        jewels = set(jewels)
        # print(jewels)
        return sum([stone in jewels for stone in stones])


assert Solution.numJewelsInStones(jewels="aA", stones="aAAbbbb") == 3
assert Solution.numJewelsInStones(jewels="z", stones="ZZ") == 0
