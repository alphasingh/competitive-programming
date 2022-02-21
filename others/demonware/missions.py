class Solution:
    @staticmethod
    def solution(D: [int], X: int) -> int:
        # D is an integer array of size N where
        # 1 <= N <= 200,000
        # 1 <= X <= 1,000,000,000
        # 1 <= D[i] <= 1,000,000,000
        days = 1
        low = high = D[0]
        for Di in D:
            low = min(low, Di)
            high = max(high, Di)
            diff = high - low
            if diff > X:  # reset
                low = high = Di
                days += 1
        return days


assert Solution.solution(D=[5, 8, 2, 7], X=3) == 3
assert Solution.solution(D=[2, 5, 9, 2, 1, 4], X=4) == 3
assert Solution.solution(D=[1, 12, 10, 4, 5, 2], X=2) == 4
assert Solution.solution(D=[1, 12, 10, 4, 5, 2], X=10) == 2
assert Solution.solution(D=[1, 12, 10, 4, 5, 2], X=11) == 1
