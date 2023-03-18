# https://leetcode.com/problems/design-browser-history/


class BrowserHistory:

    def __init__(self, homepage: str):

        self.list = [homepage]
        self.current = 0
        

    def visit(self, url: str) -> None:

        self.list = self.list[:self.current+1] + [url]
        self.current = self.current + 1
        

    def back(self, steps: int) -> str:

        self.current -= steps
        if self.current < 0:
            self.current = 0
        return self.list[self.current]
        

    def forward(self, steps: int) -> str:
        self.current += steps
        if self.current >= len(self.list):
            self.current = len(self.list) -1
        return self.list[self.current]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
