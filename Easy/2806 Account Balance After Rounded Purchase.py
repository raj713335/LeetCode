# https://leetcode.com/problems/account-balance-after-rounded-purchase/description/


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:

        purchaseAmountP = purchaseAmount
        purchaseAmountN = purchaseAmount

        while purchaseAmountP % 10 != 0 and purchaseAmountN % 10 != 0:
            purchaseAmountP += 1
            purchaseAmountN -= 1

        if purchaseAmountP % 10 == 0  and purchaseAmountN % 10 == 0:
            purchaseAmount = purchaseAmountP
        elif purchaseAmountP % 10 == 0:
            purchaseAmount = purchaseAmountP
        else:
            purchaseAmount = purchaseAmountN


        return 100-purchaseAmount 
