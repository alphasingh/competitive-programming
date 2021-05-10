"""
https://www.codechef.com/APRIL21C/problems/SOCKS1
"""


def valid_pair(socks: [int]) -> bool:
    return len(set(socks)) < 3


test_input = [5, 4, 3]  # list(map(int, input().split()))
if valid_pair(test_input):
    print('YES')
else:
    print('NO')

assert valid_pair([5, 4, 3]) is False
assert valid_pair([5, 5, 3]) is True
assert valid_pair([5, 5, 5]) is True
