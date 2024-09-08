# https://leetcode.com/problems/convert-date-to-binary/description/


class Solution:
    def convertDateToBinary(self, date: str) -> str:

        date = date.split("-")

        date[0] = bin(int(date[0]))[2:]
        date[1] = bin(int(date[1]))[2:]
        date[2] = bin(int(date[2]))[2:]

        return "-".join(date)


        
