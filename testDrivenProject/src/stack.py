class Stack:
    def __init__(self):
        self.elements = []

    def pop(self):
        result = self.elements[-1]
        del self.elements[-1]
        return result

    def push(self, n):
        if (isinstance(n, int)):
            self.elements.append(n)

    def __len__(self):
        return len(self.elements)
