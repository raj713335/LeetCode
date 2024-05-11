# https://leetcode.com/problems/design-phone-directory/


class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.__slots = set(range(maxNumbers))
        print(self.__slots)
        

    def get(self) -> int:
        if not self.__slots:
            return -1
        return self.__slots.pop()
        

    def check(self, number: int) -> bool:
        return number in self.__slots

    def release(self, number: int) -> None:
        self.__slots.add(number)

        

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
