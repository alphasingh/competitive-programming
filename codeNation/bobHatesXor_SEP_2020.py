class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        s = 0
        if B == 1 or len(A) == 1:  # max possible window size is 1
            if 0 not in set(A):
                return 1
        else:  # window size can be more than 1
            for i in range(len(A)):
                print(A[i:i + B])
                if len(set(A[i:i + B])) != len(A[i:i + B]):
                    return 0
            else:
                return 1
        return s


sol = Solution()
print(sol.solve([1, 2, 3, 1], 3))
