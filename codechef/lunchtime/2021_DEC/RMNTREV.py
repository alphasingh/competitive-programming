def romanticReversal(s: str, k: int) -> str:
    for i in range(k, 1, -1):
        s = s[:i][::-1] + s[i:]
        # print(i, s)
    return s


assert romanticReversal("yrfabet", 7) == "abferty"
assert romanticReversal("tebafry", 6) == "abferty"
assert romanticReversal("rfabety", 5) == "abferty"
assert romanticReversal("ebafrty", 4) == "abferty"
assert romanticReversal("faberty", 3) == "abferty"
assert romanticReversal("bbaaaba", 5) == "aababba"
assert romanticReversal("zxwy", 4) == "wxyz"
for T in range(int(input())):
    N, K = map(int, input().split())
    S = input()
    print(romanticReversal(S, K))
'''
https://www.codechef.com/LTIME103B/problems/RMNTREV
Time taken: 38 minutes (brute 30/100)
==========
In: 
==========
3
7 3
faberty
7 5
bbaaaba
4 4
zxwy
=======
Out:
==========
abferty
aababba
wxyz
'''

"""
working on :abferty
7 tebafry
6 rfabety
5 ebafrty
4 faberty
3 baferty
2 abferty
1 abferty
"""
