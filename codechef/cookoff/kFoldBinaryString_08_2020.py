for T in range(int(input())):
    N, K = map(int, input().split())
    S, numOfSeg, result = input(), N // K, ''
    total0, total1 = S.count('0'), S.count('1')
    if total1 % numOfSeg == 0 and total0 % numOfSeg == 0:
        numZero, numOne = total0 // numOfSeg, total1 // numOfSeg
        for segment in range(numOfSeg):
            if segment % 2 == 0:
                result += ('0' * numZero) + ('1' * numOne)
            else:
                result += ('1' * numOne) + ('0' * numZero)
    else:
        result = 'IMPOSSIBLE'
    print(result)

'''
2
8 2
00011101
6 2
100111
'''
