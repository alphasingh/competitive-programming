"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d12d7
"""

from itertools import permutations


def reversort(integers: [int], size: int) -> int:
    cost = 0
    # print(integers, size)
    for position in range(size - 1):
        minimum_element = min(integers[position:])
        minimum_element_index = integers.index(minimum_element)
        reversed_integers = integers[position: minimum_element_index + 1][::-1]
        integers = integers[:position] + reversed_integers + integers[minimum_element_index + 1:]
        cost += minimum_element_index - position + 1
        # print(integers)
    return cost


def find_permutation_with_cost(size: int, cost: int) -> str:
    output = "IMPOSSIBLE"  # if no permutation found with desired cost
    integers = [integer for integer in range(1, size + 1)]
    for permutation in list(permutations(integers)):
        cost_of_permutation = reversort(permutation, size)
        # print(permutation, cost_of_permutation)
        if cost_of_permutation == cost:
            output = ""
            for i in range(size - 1):
                output += str(permutation[i]) + " "
            output += str(permutation[-1])
            break
    # print(output)
    return output


assert find_permutation_with_cost(size=4, cost=6) == "1 3 4 2"
assert find_permutation_with_cost(size=2, cost=1) == "1 2"
assert find_permutation_with_cost(size=7, cost=12) == "1 2 3 5 7 6 4"
assert find_permutation_with_cost(size=7, cost=2) == "IMPOSSIBLE"
assert find_permutation_with_cost(size=2, cost=1000) == "IMPOSSIBLE"
assert int(True) == 0  # change to 1 to switch on custom TCs

for T in range(int(input())):
    N, C = map(int, input().split())
    print("Case #{}: {}".format(T + 1, find_permutation_with_cost(N, C)))

'''
INPUT:
5
4 6
2 1
7 12
7 2
2 1000

OUTPUT:
Case #1: 4 2 1 3
Case #2: 1 2
Case #3: 7 6 5 4 3 2 1
Case #4: IMPOSSIBLE
Case #5: IMPOSSIBLE
'''
