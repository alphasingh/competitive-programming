"""
https://leetcode.com/problems/slowest-key/
"""


class Solution:
    @staticmethod
    def slowestKey(releaseTimes: [int], keysPressed: str) -> str:
        max_duration = releaseTimes[0]
        slowest_key = keysPressed[0]
        n = len(keysPressed)
        for i in range(1, n):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            if duration == max_duration:
                slowest_key = max(slowest_key, keysPressed[i])
            elif duration > max_duration:
                slowest_key = keysPressed[i]
                max_duration = duration
        return slowest_key


assert Solution.slowestKey(releaseTimes=[9, 29, 49, 50], keysPressed="cbcd") == "c"
"""
Input: releaseTimes = [9,29,49,50], keysPressed = "cbcd"
Output: "c"
Explanation: The keypresses were as follows:
Keypress for 'c' had a duration of 9 (pressed at time 0 and released at time 9).
Keypress for 'b' had a duration of 29 - 9 = 20 
(pressed at time 9 right after the release of the previous character and released at time 29).
Keypress for 'c' had a duration of 49 - 29 = 20 
(pressed at time 29 right after the release of the previous character and released at time 49).
Keypress for 'd' had a duration of 50 - 49 = 1 
(pressed at time 49 right after the release of the previous character and released at time 50).
The longest of these was the keypress for 'b' and the second keypress for 'c', 
both with duration 20.
'c' is lexicographically larger than 'b', so the answer is 'c'.
"""

assert Solution.slowestKey(releaseTimes=[12, 23, 36, 46, 62], keysPressed="spuda") == "a"
"""
Input: releaseTimes = [12,23,36,46,62], keysPressed = "spuda"
Output: "a"
Explanation: The keypresses were as follows:
Keypress for 's' had a duration of 12.
Keypress for 'p' had a duration of 23 - 12 = 11.
Keypress for 'u' had a duration of 36 - 23 = 13.
Keypress for 'd' had a duration of 46 - 36 = 10.
Keypress for 'a' had a duration of 62 - 46 = 16.
The longest of these was the keypress for 'a' with duration 16.
"""
