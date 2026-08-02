class MyQueue:

    def __init__(self):
        self.stk = []
        self.stk2 = []

    def push(self, x:int) -> None:
        self.stk.append(x)
    
    def pop(self) -> int:
        if not self.stk2:
            while self.stk:
                self.stk2.append(self.stk.pop())
        
        return self.stk2.pop()

    def peek(self) -> int:
        if not self.stk2:
            while self.stk:
                self.stk2.append(self.stk.pop())
        
        return self.stk2[-1]
    
    def empty(self) -> bool:
        return not self.stk and not self.stk2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()