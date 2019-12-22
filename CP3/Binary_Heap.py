# Binary Heap implementation in python
# Has extra functions: deleteKey and updateKey

class Binary_Heap:

    def __init__(self, initializer):
        h = [0]
        h.extend(initializer)
        buildMaxHeap()

    def buildMaxHeap(self):
        for i in reversed(range(1, len(self.h))):
            _heapify(i, len(self.h))

    def getMax(self):
        return self.h[1]

    def popMax(self):
        self.h[1], self.h[-1] = self.h[-1], self.h[1]
        maxVal = self.h.pop()
        _heapify(1, len(self.h))
        return maxVal

    # h[idx] will "go down" the heap to its place (with location > bound) to maintain the heap property
    def _heapify(self, idx, bound):
        # won't need if I know when the leaves start
        if 2 * idx >= bound:
            return

        lc = 2 * idx
        rc = lc + 1
        swp_idx = 0
        while 2 * idx < len(self.h):
            if rc >= len(self.h):
                swp_idx = lc
            else:
                swp_idx = lc if h[lc > h[rc] else rc

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
        _heapify(idx, len(self.h))

    def updateKey(self, idx, new_key):
        # need some sort of interface
        old_key, self.h[idx] = self.h[idx], new_key
        if new_key > old_key:
            _heapify_reverse(idx, 0)
        else:
            _heapify(idx, len(self.h))
