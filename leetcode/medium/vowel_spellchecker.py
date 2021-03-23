"""
https://leetcode.com/problems/vowel-spellchecker/
"""


class Solution:
    VOWELS = {'a', 'e', 'i', 'o', 'u'}

    @staticmethod
    def isMatchIgnoringVowels(real_string: str, string_with_vowel_errors: str) -> bool:
        real_string = real_string.lower()
        string_with_vowel_errors = string_with_vowel_errors.lower()
        length_of_real_string = len(real_string)
        all_match = False
        if length_of_real_string == len(string_with_vowel_errors):
            all_match = all(string_with_vowel_errors[i] == real_string[i] or (
                    real_string[i] in Solution.VOWELS and string_with_vowel_errors[i] in Solution.VOWELS) for i in
                            range(length_of_real_string))
        return all_match

    @staticmethod
    def spellchecker(word_list: [str], queries: [str]) -> [str]:
        word_lower_map = dict()
        output = list()
        for word in word_list:
            word_lower = word.lower()
            if word_lower not in word_lower_map:
                word_lower_map[word_lower] = list()
            word_lower_map[word_lower].append(word)
        # print(word_lower_map)
        for query in queries:
            query_lower = query.lower()
            if query_lower in word_lower_map:
                list_of_possible_words = word_lower_map[query_lower]
                if query in list_of_possible_words:
                    output.append(query)
                else:
                    output.append(list_of_possible_words[0])
            else:
                for word_lower_key in word_lower_map.keys():
                    if Solution.isMatchIgnoringVowels(word_lower_key, query):
                        output.append(word_lower_map[word_lower_key][0])
                        break
                else:
                    output.append("")
        # print(output)
        return output


word_list_1 = ["KiTe", "kite", "hare", "Hare"]
queries_1 = ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]
output_1 = ["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"]
assert Solution.spellchecker(word_list=word_list_1, queries=queries_1) == output_1

"""
Example 1:
Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.

Example 2:
Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.

Note:
1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.
"""
