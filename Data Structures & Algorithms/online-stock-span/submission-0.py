class StockSpanner:

    def __init__(self):
        self.stk = []
        self.stk2 = []

    def next(self, price: int) -> int:
        count = 1
        while self.stk and self.stk[-1] <= price:
            self.stk2.append(self.stk.pop())
            count += 1
        while self.stk2:
            self.stk.append(self.stk2.pop())
        self.stk.append(price)
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)