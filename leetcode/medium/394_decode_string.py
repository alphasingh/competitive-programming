"""
https://leetcode.com/problems/decode-string/
"""


class Solution:
    @staticmethod
    def decodeString(s: str) -> str:
        c = [""]
        n = [""]
        for ch in s:
            if ch == "[":  # start nesting
                n[-1] += "#"  # end number
                c.append("")  # start new string
            elif "0" <= ch <= "9":  # digit
                if n and n[-1] and n[-1][-1] == "#":
                    n.append("")  # start new number
                n[-1] += ch  # append digit
            elif ch == "]":  # nesting ends
                last = n.pop(-1)
                if not n:
                    n.append("")
                # print(last, "l_n")
                last = last[:-1]  # remove end hash
                last = int(last)  # convert to int
                l_c = c.pop(-1)
                # print(l_c, "l_c")
                m = last * l_c  # frequency*string
                c[-1] += m
            else:
                c[-1] += ch
            # print(n, c)
        # print(n, c)
        return c[0]


assert Solution.decodeString(s="3[a]2[bc]") == "aaabcbc"
assert Solution.decodeString(s="3[a2[c]]") == "accaccacc"
assert Solution.decodeString(s="2[abc]3[cd]ef") == "abcabccdcdcdef"
assert Solution.decodeString(s="abc3[cd]xyz") == "abccdcdcdxyz"
