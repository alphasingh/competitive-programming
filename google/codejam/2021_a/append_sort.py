"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/00000000007549e5
"""


def is_possible_to_make(source: int, destination: int) -> bool:
    source, destination = str(source), str(destination)
    return destination[:len(source)] == source


def minimum_operations(integers: [int], size: int) -> int:
    operations = 0
    # print(integers)
    for i in range(size - 1):
        first = integers[i]
        second = integers[i + 1]
        if second <= first:
            if is_possible_to_make(second, first + 1):  # if possible from second
                second = first + 1
            else:  # append padding zeroes
                second = int(str(second) + '0' * (len(str(first)) - len(str(second))))
                if first >= second:  # still padding is required
                    second = int(str(second) + '0')
        operations += len(str(second)) - len(str(integers[i + 1]))
        # print(first, second)
        # print(integers)
        integers[i + 1] = second
    # print(integers)
    # print(operations)
    return operations


assert minimum_operations(integers=[100, 7, 10], size=3) == 4
assert minimum_operations(integers=[10, 10], size=2) == 1
assert minimum_operations(integers=[4, 19, 1], size=3) == 2
assert minimum_operations(integers=[1, 2, 3], size=3) == 0
assert int(True) == 0  # change to 1 to switch on custom TCs

for T in range(int(input())):
    N = int(input())
    X = list(map(int, input().split()))
    print("Case #{}: {}".format(T + 1, minimum_operations(X, N)))

'''
INPUT:
4
3
100 7 10
2
10 10
3
4 19 1
3
1 2 3
OUTPUT:
Case #1: 4
Case #2: 1
Case #3: 2
Case #4: 0
'''
