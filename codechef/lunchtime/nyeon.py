import sys

input = sys.stdin.readline

for testCase in range(int(input())):
    n = int(input())
    a = [ai for ai in str.join('', input().split()).split('1') if '0' in ai]
    # print(a)
    result = 'No'
    if len(a) == 0:
        print('No')
    else:
        for ai in a:
            if len(ai) % 2 == 0:
                print('No')
                break
        else:
            print('Yes')
'''
https://www.codechef.com/LTIME87B/problems/ARRGAME
==========
In:
==========
4
7
1 1 0 0 0 1 1
8
1 0 1 1 1 0 0 1
4
1 1 0 1
4
1 1 1 1
=======
Out:
==========
Yes
No
Yes
No
'''
