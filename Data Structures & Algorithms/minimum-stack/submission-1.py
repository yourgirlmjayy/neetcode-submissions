class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            curr_min_value = self.stack[-1][-1]
            if val < curr_min_value:
                self.stack.append((val, val))
            else:
                self.stack.append((val, curr_min_value))

    def pop(self) -> None:
        if len(self.stack) >= 1:
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack) >= 1:
            return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][-1]
#Data structures
# - min heap for getMin
# - list to store elements

# [(2, 2), (3, 2), (1, 1)]

