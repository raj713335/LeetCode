# https://leetcode.com/problems/design-compressed-string-iterator/description/


class StringIterator:

    def __init__(self, compressedString: str):
        self.stack = []

        letter = compressedString[0]

        numx = ""

        for i in range(1, len(compressedString)):
            if compressedString[i].isdigit():
                numx += compressedString[i]
            else:
                self.stack.extend([letter]*min(int(numx), 1000))
                numx = ""
                letter = compressedString[i]
        self.stack.extend([letter]*min(int(numx), 1000))


    def next(self) -> str:

        try:
            val = self.stack.pop(0)
        except:
            val = " "

        return val
        

    def hasNext(self) -> bool:

        if len(self.stack) > 0:
            return True
        else:
            return False
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
