"""
https://leetcode.com/problems/count-primes/
"""
from functools import lru_cache
from time import time


class Solution:

    @lru_cache(maxsize=5_000_000)
    def isPrime(self, x: int) -> bool:
        if x <= 1:
            return False
        i = 2
        while i * i <= x:
            if x % i == 0:
                return False
        # print(x, factors)
        return True

    def countPrimes(self, n: int) -> int:
        is_prime = [True] * n
        if n > 1:
            is_prime[0] = is_prime[1] = False
        i = 2
        while i * i < n:
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
            i += 1
        primes = 0
        for i in range(2, n):
            if is_prime[i]:
                primes += 1
        return primes


begin = time()
solution = Solution()
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
assert solution.countPrimes(5_000_000) == 348513
print(solution.isPrime.cache_info())
end = time()
print(f'Time taken {end - begin}')
