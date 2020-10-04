for testCase in range(int(input())):
    numberOfPeople, chefPosition = map(int, input().split())
    playerWhoBeatsChef = list(
        filter(lambda p: chefPosition % p == 0 and p < chefPosition, list(map(int, input().split()))))
    if len(playerWhoBeatsChef) > 0:
        print(max(playerWhoBeatsChef))
    else:
        print(-1)

'''
==========
In:
==========
2
4 6
4 3 2 8
4 7
4 3 2 8
==========
Out:
==========
3
-1
'''
