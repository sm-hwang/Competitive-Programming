# Binary Heap implementation in python
# Has extra functions: deleteKey and updateKey

class Binary_Heap:

    def __init__(self, initializer):
        self.h = [0]
        self.h.extend(initializer)
        self._buildMaxHeap()

    def _buildMaxHeap(self):
        print("in _buildMaxHeap")
        for i in reversed(range(1, len(self.h))):
            self._heapify(i, len(self.h))

    def getMax(self):
        return self.h[1]
    
    def popMax(self):
        self.h[1], self.h[-1] = self.h[-1], self.h[1]
        maxVal = self.h.pop()
        self._heapify(1, len(self.h))
        return maxVal

    # h[idx] will "go down" the heap to its place (with location > bound) to maintain the heap property
    def _heapify(self, idx, bound):
        print("in _heapify")
        # won't need if I know when the leaves start
        if 2 * idx >= bound:
            return

        lc = 2 * idx
        rc = lc + 1
        swp_idx = 0
        while 2 * idx < bound:
            if rc >= len(self.h):
                swp_idx = lc
            else:
                swp_idx = lc if self.h[lc] > self.h[rc] else rc

            if self.h[swp_idx] > self.h[idx]:
                self.h[swp_idx], self.h[idx] = self.h[idx], self.h[swp_idx]
                idx = swp_idx
            else:
                break


    # h[idx] will "go up" the heap to its place (with location > bound) to maintain the heap property
    def _heapify_reverse(self, idx, bound):
        # won't need if I know when the leaves start
        if idx // 2 <= bound:
            return

        parent = idx // 2
        swp_idx = 0
        while idx // 2 > bound:
            if self.h[parent] < self.h[idx]:
                self.h[parent], self.h[idx] = self.h[idx], self.h[parent]
                idx = parent
            else:
                break

    def deleteKey(self, idx):
        #if 0 < idx < len(self.h):
        self.h[-1], self.h[idx] = self.h[idx], self.h[-1]
        self.h.pop()
        self._heapify(idx, len(self.h))

    def updateKey(self, idx, new_key):
        # need some sort of interface
        old_key, self.h[idx] = self.h[idx], new_key
        if new_key > old_key:
            self._heapify_reverse(idx, 0)
        else:
            self._heapify(idx, len(self.h))

    # Sorts h
    def heapSort(self):
        for i in range(1, len(self.h)):
            self.h[1], self.h[-1] = self.h[-1], self.h[1]
            self._heapify(1, len(self.h) - i)

    def __repr__(self):
        print("in __repr__")
        a, *b = self.h
        return '[' + ', '.join(b) + ']'
