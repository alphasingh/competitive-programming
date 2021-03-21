def isIntersection(r: int, c: int, array: [[int]], i: int, j: int):
    has_left = has_right = has_down = has_up = False
    if i - 1 >= 0 and array[i - 1][j] == 1:  # left
        has_left = True
    if i + 1 < r and array[i + 1][j] == 1:  # right
        has_right = True
    if j - 1 >= 0 and array[i][j - 1] == 1:  # up
        has_up = True
    if j + 1 < c and array[i][j + 1] == 1:  # down
        has_down = True
    has_up_left = has_left and has_up
    has_up_right = has_right and has_up
    has_down_right = has_down and has_right
    has_down_left = has_down and has_left
    return array[i][j] and (has_up_left or has_up_right or has_down_left or has_down_right)


for T in range(int(input())):
    R, C = map(int, input().split())
    plots = [list(map(int, input().split())) for i in range(R)]
    print(plots)
    for row in range(R):
        for col in range(C):
            print(plots[row][col], (row, col), isIntersection(R, C, plots, row, col))
    print("Case #{}: {}".format(T + 1, len(plots)))

'''
INPUT:
2
4 3
1 0 0
1 0 1
1 0 0
1 1 0
6 4
1 0 0 0
1 0 0 1
1 1 1 1
1 0 1 0
1 0 1 0
1 1 1 0
OUTPUT:
Case #1: 1
Case #2: 9
'''
