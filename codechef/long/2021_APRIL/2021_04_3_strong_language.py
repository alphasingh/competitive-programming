"""
https://www.codechef.com/APRIL21C/problems/SSCRIPT
"""


def contains_strong_language(string: str, stars: int) -> bool:
    max_consecutive_stars = current = 0
    for character in string:
        if character == '*':
            current += 1
        else:
            if current > max_consecutive_stars:
                max_consecutive_stars = current
            current = 0
    return max(max_consecutive_stars, current) >= stars


assert contains_strong_language('*a*b*', 2) is False
assert contains_strong_language('*a**b', 2) is True
assert contains_strong_language('abcde', 1) is False

for T in range(int(input())):
    N, K = map(int, input().split())
    S = input()
    if contains_strong_language(S, K):
        print('YES')
    else:
        print('NO')
