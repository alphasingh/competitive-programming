def solve():
    for T in range(int(input())):
        N = int(input())
        B = list(map(int, input().split()))
        # do something
        print(B)


# solve()
a = [1, 2, 3, 3, 2, 1]
x = 54
u = set()
for i in range(1_000_000):
    m = i % x
    u.add(m)
print(u)
print(len(u))

'''
https://www.codechef.com/SNCKQL21/problems/MAXDISTKT
==========
In:
==========
3
3
2 1 3
2
1 1
6
1 2 3 3 2 1
=======
Out:
==========
3 1 2
2 3
0 1 2 3 4 5
'''
