class minMaxStack:
    def __init__(self):
        self.values = []
        self.min_val = float("inf")
        self.max_val = -float("inf")

    def pushToStack(self, val):
        self.values.append(val)
        self.max_val = max(self.max_val, val)
        self.min_val = min(self.min_val, val)

    def getMax(self):
        return self.max_val

    def getMin(self):
        return self.min_val

    def peek(self):
        return self.values[-1]

    def popStack(self):
        return self.values.pop()

    def printStack(self):
        print(self.values)


if __name__ =="__main__":
    s = minMaxStack()
    s.pushToStack(5)
    s.pushToStack(6)
    s.pushToStack(9)
    s.printStack()
    print(s.getMin())
    print(s.getMax())
    print(s.popStack())
    s.printStack()
