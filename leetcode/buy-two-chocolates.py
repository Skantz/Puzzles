class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a = min(prices)
        prices.remove(a)
        b = min(prices)
        if a + b > money:
            return money
        return money - a - b
