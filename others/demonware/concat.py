class Solution:
    @staticmethod
    def solution(strings: [str]) -> [str]:
        n = len(strings)
        result = []
        for i in range(1, n):
            result.append(strings[i - 1][0] + strings[i][-1])
        result.append(strings[-1][0] + strings[0][-1])
        # print(result)
        return result


assert Solution.solution(['cat', 'dog', 'ferret', 'scorpion']) == ['cg', 'dt', 'fn', 'st']
