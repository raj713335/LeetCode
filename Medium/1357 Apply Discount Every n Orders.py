# https://leetcode.com/problems/apply-discount-every-n-orders/


class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.customer_id = 0
        self.n = n
        self.discount = 100-discount
        self.products_list = {}
        
        for i in range(0, len(products)):
            self.products_list[products[i]] = prices[i]
        
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_id += 1
        bill = 0
        
        for i in range(0, len(product)):
            bill += (self.products_list[product[i]] * amount[i])
            
        if self.customer_id % self.n == 0:
            bill = bill * (self.discount/100)
            
        return bill
        
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
