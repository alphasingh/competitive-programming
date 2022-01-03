"""
https://leetcode.com/problems/find-the-town-judge/
"""


class Solution:
    @staticmethod
    def findJudge(n: int, trust: [[int]]) -> int:
        votes = {person: set() for person in range(1, n + 1)}
        for person in trust:
            votes[person[0]].add(person[1])
        # print(votes)
        judge = -1
        # find probable judge
        for person, trusts in votes.items():
            if not trusts:
                judge = person
                break
        # print(votes, judge)
        # confirm probable judge
        if judge in votes:
            del votes[judge]
        # print(votes, judge)
        for person in votes:
            if judge not in votes[person]:
                judge = -1
                break
        return judge


assert Solution.findJudge(n=2, trust=[[1, 2]]) == 2
assert Solution.findJudge(n=3, trust=[[1, 3], [2, 3]]) == 3
assert Solution.findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]) == -1
