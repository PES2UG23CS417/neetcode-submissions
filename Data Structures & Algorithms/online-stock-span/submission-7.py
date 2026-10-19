class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 0
        self.stack.append(price)
        i = len(self.stack) - 1
        while i > -1 and self.stack[i] <= price:
            span += 1
            i -= 1
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)