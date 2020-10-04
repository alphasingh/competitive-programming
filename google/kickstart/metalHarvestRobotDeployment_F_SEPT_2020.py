import math

for T in range(int(input())):
    N, K = map(int, input().split())
    robotsRequired = robotStart = robotEnd = 0
    intervals = []
    for i in range(N):
        intervals.append(tuple(map(int, input().split())))  # start, end
    intervals.sort()
    # print(intervals)
    for interval in intervals:
        if not (interval[0] <= robotEnd and interval[1] <= robotEnd):
            if robotEnd < interval[0]:
                robotStart = interval[0]
            else:
                robotStart = robotEnd
            robotsForInterval = math.ceil((interval[1] - robotStart) / K)
            robotsRequired += robotsForInterval
            robotEnd = robotStart + (K * robotsForInterval)
            # print((robotsForInterval, robotStart, robotEnd), end=' ')
    print("Case #{}: {}".format(T + 1, robotsRequired))

'''
INPUT:
6
3 5
1 5
10 11
8 9
3 2
1 2
3 5
13 14
5 5
1 3
8 9
10 11
12 17
4 6
1 3
3 12
1 4
1 10
5 5
1 3
8 9
10 11
12 30
4 6
OUTPUT:
Case #1: 2
Case #2: 3
Case #3: 3
Case #4: 3
Case #5: 3
Case #6: 6
'''
