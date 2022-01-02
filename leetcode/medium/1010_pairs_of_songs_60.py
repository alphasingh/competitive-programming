"""
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
"""


class Solution:
    @staticmethod
    def numPairsDivisibleBy60(times: [int]) -> int:
        sums = (60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960)
        count = dict()
        for time in times:
            if time not in count:
                count[time] = 0
            count[time] += 1
        # print(count)
        pairs = 0
        for time in times:
            for target in sums:
                second = target - time
                if second in count and count[second] > 0:
                    pairs += count[second]
                    if second == time:
                        pairs -= 1
                    # print(pairs)
            count[time] -= 1
        return pairs


assert Solution.numPairsDivisibleBy60([30, 20, 150, 100, 40]) == 3
"""
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
"""
assert Solution.numPairsDivisibleBy60([60, 60, 60]) == 3
"""
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
"""
