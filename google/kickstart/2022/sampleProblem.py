"""
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000942404
"""


# returns remaining candies after distributing
def candiesLeft(candies: [int], kids: int) -> int:
    total_candies = sum(candies)
    each_kid_gets = total_candies // kids
    candies_given = each_kid_gets * kids
    return total_candies - candies_given


assert candiesLeft([1, 2, 3, 4, 5, 6, 7], 3) == 1
assert candiesLeft([7, 7, 7, 7, 7], 10) == 5

# for T in range(int(input())):
#     N, M = map(int, input().split())
#     C = list(map(int, input().split()))
#     L = candiesLeft(C, M)
#     print("Case #{}: {}".format(T + 1, L))

"""
2
7 3
1 2 3 4 5 6 7
5 10
7 7 7 7 7
"""
"""
Case #1: 1
Case #2: 5
"""
