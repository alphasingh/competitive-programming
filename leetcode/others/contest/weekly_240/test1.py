"""
https://leetcode.com/contest/weekly-contest-236/problems/find-the-winner-of-the-circular-game/
"""


class Solution:
    def maximumPopulation(self, logs: [[int]]) -> int:
        max_pop = 0
        max_year = 1950
        for year in range(1950, 2051):
            current_pop = 0
            for log in logs:
                if log[0] <= year < log[1]:
                    current_pop += 1
                    if current_pop > max_pop:
                        max_pop = current_pop
                        max_year = year
        return max_year


sol = Solution()
assert sol.maximumPopulation([[1993, 1999], [2000, 2010]]) == 1993
assert sol.maximumPopulation([[1950, 1961], [1960, 1971], [1970, 1981]]) == 1960
assert sol.maximumPopulation(
    [[2008, 2026], [2004, 2008], [2034, 2035], [1999, 2050], [2049, 2050], [2011, 2035], [1966, 2033],
     [2044, 2049]]) == 2011
