from itertools import combinations


class Solution:

    @staticmethod
    def combination_possible(n, combination) -> bool:
        in_degree = out_degree = [0] * n
        for node in combination:
            out_degree[node[0]] += 1
            in_degree[node[1]] += 1
        print(combination, in_degree, out_degree)
        return in_degree == out_degree

    @staticmethod
    def maximum_requests(n: int, requests: [[int]]) -> int:
        # print(n, requests)
        maximum_requests = 0
        for requestsIncluded in range(1, len(requests) + 1):
            for combination in list(combinations(requests, requestsIncluded)):
                if Solution.combination_possible(n, combination):
                    maximum_requests = requestsIncluded
                    continue
        return maximum_requests


sol = Solution()
print(sol.maximum_requests(3, [[0, 1], [0, 0], [1, 0]]))
