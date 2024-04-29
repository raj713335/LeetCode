# https://leetcode.com/problems/count-houses-in-a-circular-street/description/

# Definition for a street.
# class Street:
#     def openDoor(self):
#         pass
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
#     def moveLeft(self):
#         pass
class Solution:
    def houseCount(self, street: Optional['Street'], k: int) -> int:

        for i in range(0, k):
            if street.isDoorOpen():
                street.closeDoor()
            street.moveLeft()
        count = 0
        for i in range(0, k):
            if street.isDoorOpen():
                break
            street.openDoor()
            street.moveLeft()
            count += 1;
        return count
        
