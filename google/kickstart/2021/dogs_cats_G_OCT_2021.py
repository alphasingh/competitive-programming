for T in range(int(input())):
    N, D, C, M = map(int, input().split())
    S = input()  # animals in line
    if M > N:
        M = N
    dogs = S.count('D')
    all_dogs_fed = 'YES'
    for animal in S:
        if animal == 'C' and C > 0:  # feed cat
            C -= 1
        elif animal == 'D' and D > 0:  # feed dog
            C = min(N, C + M)
            D -= 1
            dogs -= 1
        else:  # cannot feed anymore
            break
    if dogs > 0:
        all_dogs_fed = 'NO'
    print("Case #{}: {}".format(T + 1, all_dogs_fed))

'''
https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b3771
================
INPUT:
================
5
6 10 4 0
CCDCDD
4 1 2 0
CCCC
4 2 1 0
DCCD
12 4 2 2
CDCCCDCCDCDC
8 2 1 3
DCCCCCDC
================
OUTPUT:
================
Case #1: YES
Case #2: YES
Case #3: NO
Case #4: YES
Case #5: NO
================
'''
