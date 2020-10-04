import math
import sys

input = sys.stdin.readline

for testCase in range(int(input())):
    initialDarthHealth, initialChefAttackPower = map(int, input().split())
    chefCanBeatDarth = 0
    numberOfAttacksPossible = math.floor(math.log2(initialChefAttackPower))
    totalAttackPowerPossible = 2 * initialChefAttackPower * (1 - 0.5 ** numberOfAttacksPossible) + 1
    if totalAttackPowerPossible >= initialDarthHealth:
        chefCanBeatDarth = 1
    print(chefCanBeatDarth)

'''
https://www.codechef.com/problems/CHEFWARS
==========
In:
==========
2
10 4
10 8
=======
Out:
==========
0
1
'''
