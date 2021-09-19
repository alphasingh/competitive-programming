for T in range(int(input())):
    D, N, K = map(int, input().split())
    attractions = []
    max_happiness = 0
    if N > 1000 or D > 1000:
        print("Case #{}: {}".format(T + 1, max_happiness))
        continue
    for attraction in range(N):
        h, s, e = map(int, input().split())  # happiness, start, end
        attractions.append((h, s, e))
    attractions.sort()
    for day in range(1, D + 1):
        day_total_happiness = 0
        day_attractions_taken = 0
        for attraction in attractions[::-1]:
            if day_attractions_taken == K:  # max allowed attractions
                break
            if attraction[1] <= day <= attraction[2]:
                day_total_happiness += attraction[0]
                day_attractions_taken += 1
        # print(day, day_total_happiness)
        max_happiness = max(max_happiness, day_total_happiness)
    print("Case #{}: {}".format(T + 1, max_happiness))

'''
================
INPUT:
================
2
10 4 2
800 2 8
1500 6 9
200 4 7
400 3 5
5 3 3
400 1 3
500 5 5
300 2 3
================
OUTPUT:
================
Case #1: 2300
Case #2: 700
================
'''
