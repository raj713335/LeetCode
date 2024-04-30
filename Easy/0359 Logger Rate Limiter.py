# https://leetcode.com/problems/logger-rate-limiter/description/


class Logger:

    def __init__(self):
        self.dictx = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        if message not in self.dictx:
            self.dictx[message] = timestamp + 10
            return True
        else:
            if self.dictx[message] <= timestamp:
                self.dictx[message] = timestamp + 10
                return True
            else:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
