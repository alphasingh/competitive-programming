from collections import Counter
import sys

input = sys.stdin.readline

for testCase in range(int(input())):
    n, m = map(int, input().split())
    ratings = list(map(int, input().split()))
    players = [list() for player in range(n)]
    for player in range(n):
        changes = list(map(int, input().split()))
        rating = ratings[player]
        for change in changes:
            rating += change
            players[player].append(rating)
    # print(players)
    s = 0
    sortedRatings = list()
    for month in range(m):
        ratingsForMonth = dict()
        for player in range(n):
            ratingsForMonth[player] = players[player][month]
        sortedRatings.append(sorted(ratingsForMonth, reverse=True))
    # print('sortedRatingPerMonth', sortedRatings)
    for player in range(n):
        maxRatingMonth = players[player].index(max(players[player]))
        # print('player', player)
        rankingsOfPlayer = list()
        for month in range(m):
            rankingInMonth = ratingsForMonth[player]
            # print(players[player][month], month, 'ranking ', rankingInMonth)
            rankingsOfPlayer.append(rankingInMonth)
        maxRankingMonth = rankingsOfPlayer.index(min(rankingsOfPlayer))
        # print('maxRatingMonth', maxRatingMonth, 'maxRanking', maxRankingMonth)
        if maxRankingMonth != maxRatingMonth:
            s += 1
        # playerRatingsInMaxMonth = list()
        # for p in range(n):
        #     playerRatingsInMaxMonth.append(players[p][monthOfMax])
        # print(m, 'indexMax', monthOfMax, "playerRatings in month", playerRatingsInMaxMonth)
        # sortedRatings = sorted(playerRatingsInMaxMonth)
        # if max(playerRatingsInMaxMonth) != m:
        #     s += 1
        #     print('not max in same month')

    print(s)

'''
https://www.codechef.com/LTIME87B/problems/ELOMAX
==========
In:
==========
2
3 3
2500 2500 2520
10 -5 -20
10 15 20
-15 17 13
2 3
2125 2098
-20 10 -10
10 10 -20
=======
Out:
==========
2
2
'''
