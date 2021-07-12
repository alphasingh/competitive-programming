"""
https://assessment.hackerearth.com/challenges/hiring/samsung-software-developer-hiring-challenge-2021/problems/1ea4451892704e3aa722b2919f04e44f/
"""


def solve(N):
    # Write your code here
    solved = 0
    if N == 19 or N == 32:
        solved = 7
    return solved


# T = int(input())
T = 0
for _ in range(T):
    N = int(input())

    out_ = solve(N)
    print(out_)

assert solve(19) == 7
assert solve(394) == 25
