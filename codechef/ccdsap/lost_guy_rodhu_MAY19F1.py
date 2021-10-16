for T in range(int(input())):
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    queries = list(map(int, input().split()))
    maximums = A.copy()
    running_max = maximums[0]
    for i in range(N):
        running_max = max(maximums[i], running_max)
        maximums[i] = running_max
    # print(maximums)
    for query in queries:
        print(maximums[query - 1])

'''
1        
5 3        
5 4 8 6 9        
2 3 5
=====
5        
8        
9  
'''
