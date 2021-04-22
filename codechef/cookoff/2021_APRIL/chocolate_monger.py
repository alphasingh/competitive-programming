for T in range(int(input())):
    n, x = map(int, input().split())
    A = list(map(int, input().split()))
    can_eat = 0
    for chocolates in set(A):
        if x == n:
            break
        n -= 1
        can_eat += 1
    # print(min(n - x, len(set(A))))
    print(can_eat)

'''
3
2 1
1 2
4 2
1 1 1 1
5 3
50 50 50 100 100
=======
1
1
2
'''
