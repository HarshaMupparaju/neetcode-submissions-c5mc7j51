class MyQueue:

    def __init__(self):
        self.st1 = [] #Push Stack
        self.st2 = [] #Pop stack

    def push(self, x: int) -> None:

        while(len(self.st2) > 0):
            self.st1.append(self.st2.pop())

        self.st1.append(x)
        return

    def pop(self) -> int:
        while(len(self.st1) > 0):
            self.st2.append(self.st1.pop())

        return self.st2.pop()

    def peek(self) -> int:
        while(len(self.st1) > 0):
            self.st2.append(self.st1.pop())

        return self.st2[-1]

    def empty(self) -> bool:
        if(len(self.st1) == 0 and len(self.st2) == 0):
            return True
        
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()