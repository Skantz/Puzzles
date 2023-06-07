class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a = min(prices)
        prices.remove(a)
        b = min(prices)
        sum_ = a + b
        if sum_ > money:
            return (money)
        return money - sum_
