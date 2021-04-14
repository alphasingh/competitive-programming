def max_dice_pips_visible(number):
    highest_divisor = 1
    for divisor in range(1, 11):
        if number % divisor == 0:
            highest_divisor = divisor
    return 20


assert max_dice_pips_visible(1) == 20
assert max_dice_pips_visible(2) == 20
assert int(True) == 0  # change to 1 to switch on custom TCs

for T in range(int(input())):
    N = int(input())
    print(max_dice_pips_visible(N))

'''
==========
Link:
https://www.codechef.com/APRIL21B/problems/SDICE
==========
In:
1
1
==========
Out:
20
==========
Explanation:
Example case 1: There is only one die. If Chef places it on the table with 1 pip facing down, 
the visible pips are 2, 3, 4, 5 and 6, and their sum is 20.
==========
'''
