"""
https://leetcode.com/problems/task-scheduler/
"""


class Solution:
    alphabets = 'abcdefghijklmnopqrstuvwxyz'.upper()

    def leastInterval(self, tasks: [str], n: int) -> int:
        total_time = len(tasks)
        frequency_of_alphabets = {alphabet: 0 for alphabet in self.alphabets}
        for task in tasks:
            frequency_of_alphabets[task] += 1
        frequency_of_alphabets = list(frequency_of_alphabets.values())
        max_alphabet_frequency = max(frequency_of_alphabets)
        # print(frequency_of_alphabets)
        fillers = (max_alphabet_frequency - 1) * n
        frequency_of_alphabets.remove(max_alphabet_frequency)
        # print(frequency_of_alphabets)
        for frequency_of_alphabet in frequency_of_alphabets:
            fillers -= min(max_alphabet_frequency - 1, frequency_of_alphabet)
        # print(fillers)
        if fillers < 0:
            fillers = 0
        total_time += fillers
        # print('time:', total_time)
        return total_time


sol = Solution()

assert sol.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2) == 8
"""
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
"""
assert sol.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=0) == 6
"""
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
"""
assert sol.leastInterval(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2) == 16
"""
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
"""
assert sol.leastInterval(["A", "C", "C", "C", "C", "A", "A", "B", "B", "B"], n=3) == 13
