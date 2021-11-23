"""
https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
"""


class Solution:
    @staticmethod
    def modifyString(s: str) -> str:
        s_list = list(s)
        alphabets = set('abcdefghijklmnopqrstuvwxyz')
        # print(l)
        size = len(s_list)
        for i in range(size):
            if s_list[i] == '?':
                different = alphabets.difference({s_list[i - 1], s_list[(i + 1) % size]})
                # print(different, {l[i-1], l[(i+1)%size]})
                s_list[i] = list(different)[0]
        # print(l)
        return ''.join(s_list)


assert Solution.modifyString("?zs") != "zzs"
"""
Explanation: There are 25 solutions for this problem. 
From "azs" to "yzs", all are valid. 
Only "z" is an invalid modification as the string will 
consist of consecutive repeating characters in "zzs".
"""
s2 = Solution.modifyString("ubv?w")
assert s2 != "ubvww" and s2 != "ubvvw"
"""
Explanation: There are 24 solutions for this problem. 
Only "v" and "w" are invalid modifications as the strings 
will consist of consecutive repeating characters in "ubvvw" and "ubvww".
"""
"""
Example 3:
Input: s = "j?qg??b"
Output: "jaqgacb"

Example 4:
Input: s = "??yw?ipkj?"
Output: "acywaipkja"
"""
