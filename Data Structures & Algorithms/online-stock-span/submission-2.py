class StockSpanner:

    def __init__(self):
        self.stk = []
        self.stk2 = []
        tracker = []

    def next(self, price: int) -> int:
        if not self.stk:
            self.stk.append([price, 1])
        else:
            count = 1
            while self.stk and self.stk[-1][0] <= price:
                count += self.stk.pop()[1]
            self.stk.append([price, count])
        
        return self.stk[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)