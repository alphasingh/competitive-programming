"""
https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/
"""


class Solution:
    @staticmethod
    def minTimeToType(word: str) -> int:
        # circle = 'abcdefghijklmnopqrstuvwxyz'
        pointer = 0
        time = 0
        for alphabet in word:
            index = ord(alphabet) - ord('a')
            if index != alphabet:
                if index > pointer:  # alphabet on right
                    clockwise_distance = index - pointer
                    anti_clockwise_distance = pointer + (26 - index)
                else:  # alphabet on left
                    clockwise_distance = index + (26 - pointer)
                    anti_clockwise_distance = pointer - index
                # print(index, alphabet)
                # print(clockwise_distance, anti_clockwise_distance)
                time += min(clockwise_distance, anti_clockwise_distance)
                pointer = index
            time += 1
        # print(time)
        return time


assert Solution.minTimeToType("abc") == 5
"""
Explanation: 
The characters are printed as follows:
- Type the character 'a' in 1 second since the pointer is initially on 'a'.
- Move the pointer clockwise to 'b' in 1 second.
- Type the character 'b' in 1 second.
- Move the pointer clockwise to 'c' in 1 second.
- Type the character 'c' in 1 second.
"""
assert Solution.minTimeToType("bza") == 7
"""
Explanation:
The characters are printed as follows:
- Move the pointer clockwise to 'b' in 1 second.
- Type the character 'b' in 1 second.
- Move the pointer counterclockwise to 'z' in 2 seconds.
- Type the character 'z' in 1 second.
- Move the pointer clockwise to 'a' in 1 second.
- Type the character 'a' in 1 second.
"""
assert Solution.minTimeToType("zjpc") == 34
"""
Explanation:
The characters are printed as follows:
- Move the pointer counterclockwise to 'z' in 1 second.
- Type the character 'z' in 1 second.
- Move the pointer clockwise to 'j' in 10 seconds.
- Type the character 'j' in 1 second.
- Move the pointer clockwise to 'p' in 6 seconds.
- Type the character 'p' in 1 second.
- Move the pointer counterclockwise to 'c' in 13 seconds.
- Type the character 'c' in 1 second.
"""
