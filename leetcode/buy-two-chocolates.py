class Solution:
    def buyChoco(self, prices, money: int) -> int:
        a = min(prices)
        prices.remove(a)
        b = min(prices)
        if money < a + b:
            return money
        return money - a - b
