"""
https://leetcode.com/problems/task-scheduler/
"""


class Solution:
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    def leastInterval(self, tasks: [str], n: int) -> int:
        total_time = len(tasks)
        frequency_of_alphabet = {alphabet: 0 for alphabet in self.alphabets}
        print(frequency_of_alphabet, n)
        return total_time


sol = Solution()

assert sol.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2) == 8
"""
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
"""
assert sol.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2) == 6
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
