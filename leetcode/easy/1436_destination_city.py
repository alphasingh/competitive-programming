"""
https://leetcode.com/problems/destination-city/
"""


class Solution:
    @staticmethod
    def destCity(paths: [[str]]) -> str:
        sources = set()
        destinations = set()
        for path in paths:
            sources.add(path[0])
            destinations.add(path[1])
        return list(destinations.difference(sources))[0]


assert Solution.destCity(paths=[["London", "New York"],
                                ["New York", "Lima"],
                                ["Lima", "Sao Paulo"]]) == "Sao Paulo"
"""
Explanation: Starting at "London" city you will reach "Sao Paulo" city 
which is the destination city. 
Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
"""
assert Solution.destCity(paths=[["B", "C"],
                                ["D", "B"],
                                ["C", "A"]]) == "A"
"""
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
"""
assert Solution.destCity(paths=[["A", "Z"]]) == "Z"
