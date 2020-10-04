"""
933. Number of Recent Calls
https://leetcode.com/problems/number-of-recent-calls/
"""


class RecentCounter:

    def __init__(self):
        self.pointer = 0
        self.counter = 0
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.counter += 1
        for i in range(self.pointer, self.counter):
            # print(self.requests, self.pointer)
            if self.requests[i] < t - 3000:
                self.pointer += 1
            else:
                break
        return self.counter - self.pointer


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

"""
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
"""
