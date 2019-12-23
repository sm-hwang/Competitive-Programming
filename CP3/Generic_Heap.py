import operator

# if self.compare = operator.gt, is max heap
# if self.compare = operator.lt, is min heap
class Binary_Heap:

    def __init__(self, initializer=(), compare=operator.gt):
        self._h = [None] 
        self._compare = compare
        self._h.extend(initializer)
        self._buildHeap()
    
    def _buildHeap(self):
        # last non-leaf node is at n//2 - 1 if 0-based index, so
        # for 1-based is n//2 
        for i in reversed(range(1, len(self._h)//2 + 1)):
            self._heapify(i, len(self._h))

    def insert(self, new_el):
        self._h.append(new_el)
        self._heapify_reverse(len(self._h) - 1, 0)

    def getMax(self):
        return self._h[1] 

    def popMax(self):
        self._h[1], self._h[-1] = self._h[-1], self._h[1]
        maxVal = self._h.pop()
        self._heapify(1, len(self._h))
        return maxVal

    # h[idx] will "go down" the heap to its place (with location > bound) to maintain the heap property
    def _heapify(self, idx, bound):
        # won't need if I know when the leaves start
        if 2 * idx >= bound:
            return 
    
        swp_idx = 0
        while 2 * idx < bound:
            lc = 2 * idx
            rc = lc + 1
            if rc >= bound:
                swp_idx = lc
            else:
                swp_idx = lc if self._compare(self._h[lc],self._h[rc]) else rc
            if self._compare(self._h[swp_idx], self._h[idx]):
                self._h[swp_idx], self._h[idx] = self._h[idx], self._h[swp_idx]
                idx = swp_idx
            else:
                break
            
    # h[idx] will "go up" the heap to its place (with location > bound) to maintain the heap property
    def _heapify_reverse(self, idx, bound):
        # won't need if I know when the leaves start
        if idx // 2 <= bound:
            return 

        swp_idx = 0
        while idx // 2 > bound:
            parent = idx // 2
            if self._compare(self._h[idx], self._h[parent]):
                self._h[parent], self._h[idx] = self._h[idx], self._h[parent]
                idx = parent
            else:
                break

    def deleteKey(self, idx):
        self._h[-1], self._h[idx] = self._h[idx], self._h[-1]
        self._h.pop()
        self._heapify(idx, len(self._h))
            
    def updateKey(self, idx, new_key):
        old_key, self._h[idx] = self._h[idx], new_key
        if self._compare(new_key, old_key):
            self._heapify_reverse(idx, 0)
        else:
            self._heapify(idx, len(self._h))

    # Sorts h if self._compare == operator.gt
    # Still buggy
    def heapSort(self):
        for i in range(1, len(self._h)):
            self._h[1], self._h[-i] = self._h[-i], self._h[1]
            self._heapify(1, len(self._h) - i - 1)

    def __repr__(self):
        a, *b = self._h
        return '[' + ', '.join(map(str,b)) + ']'

    def __len__(self):
        return len(self._h) - 1
