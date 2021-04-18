"""
https://leetcode.com/problems/group-anagrams/
"""


class Solution:

    def groupAnagrams(self, strs: [str]) -> [[str]]:
        groups = dict()
        for string in strs:
            anagram_hash = tuple(sorted(string)).__hash__()
            if anagram_hash not in groups:
                groups[anagram_hash] = []
            groups[anagram_hash].append(string)
        # print(list(groups.values()))
        return list(groups.values())


sol = Solution()

input_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
output_1 = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
assert sol.groupAnagrams(strs=input_1) == output_1

input_1 = [""]
output_1 = [[""]]
assert sol.groupAnagrams(strs=input_1) == output_1

input_1 = ["a"]
output_1 = [["a"]]
assert sol.groupAnagrams(strs=input_1) == output_1
