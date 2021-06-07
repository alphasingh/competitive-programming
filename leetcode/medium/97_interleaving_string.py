"""
https://leetcode.com/problems/interleaving-string/
"""


class Solution:

    @staticmethod
    def isInterleave(s1: str, s2: str, s3: str) -> bool:
        is_s3_possible = False
        pointer1 = pointer2 = 0
        length_s1 = len(s1)
        length_s2 = len(s2)
        print(length_s1, length_s2)
        for character in s3:
            print(character, pointer1, pointer2)
            if pointer1 < length_s1 and s1[pointer1] == character:
                pointer1 += 1
            elif pointer2 < length_s2 and s2[pointer2] == character:
                pointer2 += 1
            else:
                break
        print(pointer1, pointer2)
        return is_s3_possible


assert Solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac") is True
assert Solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc") is False
assert Solution.isInterleave(s1="", s2="", s3="") is True
