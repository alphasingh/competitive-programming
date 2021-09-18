# for T in range(int(input())):
#     recordBreakingDays = maxVisitorsOnADay = 0
#     totalNumberOfDays = int(input())
#     visitorsOnDays = list(map(int, input().split()))
#     for day in range(totalNumberOfDays):
#         visitorsOnDay = visitorsOnDays[day]
#         if visitorsOnDay > maxVisitorsOnADay:
#             maxVisitorsOnADay = visitorsOnDay
#             if (day == totalNumberOfDays - 1) or (visitorsOnDay > visitorsOnDays[day + 1]):
#                 recordBreakingDays += 1
#     print("Case #{}: {}".format(T + 1, recordBreakingDays))


for T in range(int(input())):
    recordBreaksCount = previousRecord = 0
    totalNumberOfDays = int(input())
    visitors = list(map(int, input().split()))
    for i in range(totalNumberOfDays):
        greaterThanPreviousDays = (i == 0 or visitors[i] > previousRecord)
        greaterThanFollowingDay = ((i == totalNumberOfDays - 1) or visitors[i] > visitors[i + 1])
        if greaterThanPreviousDays and greaterThanFollowingDay:
            recordBreaksCount += 1
        previousRecord = max(previousRecord, visitors[i])
    print("Case #{}: {}".format(T + 1, recordBreaksCount))
