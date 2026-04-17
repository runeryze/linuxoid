class MyQueue:

    def __init__(self):
        self.ins = []
        self.outs = []

    def push(self, x):
        self.ins.append(x)

    def pop(self):
        if not self.outs:
            while self.ins:
                self.outs.append(self.ins.pop())
        return self.outs.pop()

    def peek(self):
        if not self.outs:
            while self.ins:
                self.outs.append(self.ins.pop())
        return self.outs[-1]

    def empty(self):
        return len(self.ins) == 0 and len(self.outs) == 0
