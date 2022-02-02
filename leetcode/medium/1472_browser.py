"""
https://leetcode.com/contest/weekly-contest-192/problems/design-browser-history/
"""


class BrowserHistory:

    def __init__(self, homepage: str):
        self.visited = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        # forget forward history
        self.visited = self.visited[:self.current + 1]
        self.visited.append(url)
        self.current = len(self.visited) - 1
        # print(self.visited)

    def back(self, steps: int) -> str:
        can_back = self.current
        after_backing = 0 if steps > can_back else (self.current - steps)
        self.current = after_backing
        return self.visited[self.current]

    def forward(self, steps: int) -> str:
        end = len(self.visited) - 1
        can_forward = end - self.current
        after_forwarding = end if steps > can_forward else (self.current + steps)
        self.current = after_forwarding
        return self.visited[self.current]


"""
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]
"""

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
