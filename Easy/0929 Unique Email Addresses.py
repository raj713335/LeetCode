# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        dictx = {}

        for each in emails:
            temp = each.split("@")
            temp[0] = temp[0].replace(".", "")
            try:
                index = temp[0].index("+")
                temp[0] = temp[0][:index]
            except:
                pass
            email = temp[0]+"@"+temp[1]
            print(email)
            dictx[email] = 1

        return len(dictx)
