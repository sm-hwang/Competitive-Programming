# Stack implementation
# With additional O(n) space, can know max element in the stack in O(1) time with peakMax()
class Stack:

    def __init__(self, initializer):
        self._q = []
        self._maxes = []
        for i in initializer:
            self.push(i)
        
    def peak(self):
        return self._q[-1]

    def pop(self):
        el = self._q.pop()
        if el == self._maxes[-1]:
            self._maxes.pop()
        return el

    def push(self, new_el):
        if not self._q or new_el >= self._maxes[-1]:
            self._maxes.append(new_el)
        self._q.append(new_el)

    def peakMax(self):
        return self._maxes[-1]
