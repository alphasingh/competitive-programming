"""
https://leetcode.com/problems/count-primes/
"""
from time import time


class Solution:
    is_prime = [True] * 5_000_000

    def countPrimes(self, n: int) -> int:
        if n > 1:
            self.is_prime[0] = self.is_prime[1] = False
        i = 2
        while i * i < n:
            if self.is_prime[i]:
                for j in range(i * i, n, i):
                    self.is_prime[j] = False
            i += 1
        primes = 0
        for i in range(2, n):
            if self.is_prime[i]:
                primes += 1
        return primes


begin = time()
solution = Solution()
assert solution.countPrimes(5_000_000) == 348513
assert solution.countPrimes(10) == 4
assert solution.countPrimes(0) == 0
assert solution.countPrimes(1) == 0
assert solution.countPrimes(2) == 0
assert solution.countPrimes(43) == 13
assert solution.countPrimes(560) == 102
assert solution.countPrimes(560) == 102
assert solution.countPrimes(1_000) == 168
assert solution.countPrimes(9) == 4
assert solution.countPrimes(3) == 1
assert solution.countPrimes(1_0_000) == 1229
assert solution.countPrimes(1_0_000) == 1229
assert solution.countPrimes(1_0_000) == 1229
assert solution.countPrimes(1_00_000) == 9592
assert solution.countPrimes(1_00_000) == 9592
assert solution.countPrimes(1_000_000) == 78498
assert solution.countPrimes(1_000_000) == 78498
end = time()
print(f'Time taken {end - begin}')
