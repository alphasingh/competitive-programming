"""
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000941ec5
"""


# returns ruler name for given kingdom
def ruler(kingdom_name: str) -> str:
    last_letter = kingdom_name[-1].lower()
    if last_letter == "y":
        ruler_for_kingdom = "nobody"
    elif last_letter in "aeiou":
        ruler_for_kingdom = "Alice"
    else:
        ruler_for_kingdom = "Bob"
    return ruler_for_kingdom


assert ruler("Mollaristan") == "Bob"
assert ruler("B") == "Bob"
assert ruler("Auritania") == "Alice"
assert ruler("O") == "Alice"
assert ruler("Zizily") == "nobody"
assert ruler("Y") == "nobody"

# for T in range(int(input())):
#     K = input()
#     Y = ruler(K)
#     print("Case #{}: {} is ruled by {}.".format(T + 1, K, Y))

"""
3
Mollaristan
Auritania
Zizily
"""
"""
Case #1: Mollaristan is ruled by Bob.
Case #2: Auritania is ruled by Alice.
Case #3: Zizily is ruled by nobody.
"""
