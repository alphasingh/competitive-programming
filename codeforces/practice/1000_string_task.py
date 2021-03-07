vowels = {"a", "o", "y", "e", "u", "i"}

string_input = input().lower()
string_output = ""
for char in string_input:
    if char not in vowels:
        string_output += "." + char.lower()
print(string_output)

'''
==========
Link:
https://codeforces.com/problemset/problem/118/A
==========
In:
tour
Codeforces
aBAcAba
==========
Out:
.t.r
.c.d.f.r.c.s
.b.c.b
==========
'''
