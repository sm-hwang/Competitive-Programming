# Max Binary_Heap Implementation
# Has functions deleteKey and updateKey
class Binary_Heap:

    def __init__(self, initializer):
        self.h = [0]
        self.h.extend(initializer)
        self._buildMaxHeap()
    
    def _buildMaxHeap(self):
        for i in reversed(range(1, len(self.h))):
            self._heapify(i, len(self.h))

    def insert(self, new_el):
        self.h.append(new_el)
        self._heapify_reverse(len(self.h) - 1, 0)

    def getMax(self):
        return self.h[1] 

    def popMax(self):
        self.h[1], self.h[-1] = self.h[-1], self.h[1]
        maxVal = self.h.pop()
        self._heapify(1, len(self.h))
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

        swp_idx = 0
        while idx // 2 > bound:
            parent = idx // 2
            if self.h[parent] < self.h[idx]:
                self.h[parent], self.h[idx] = self.h[idx], self.h[parent]
                idx = parent
            else:
                break
    
    # Deletes key at idx (1 based)
    def deleteKey(self, idx):
        #if 0 < idx < len(self.h):
        self.h[-1], self.h[idx] = self.h[idx], self.h[-1]
        self.h.pop()
        self._heapify(idx, len(self.h))
    
    # Updates key at idx (1 based)
    def updateKey(self, idx, new_key):
        old_key, self.h[idx] = self.h[idx], new_key
        print(old_key)
        if new_key > old_key:
            self._heapify_reverse(idx, 0)
        else:
            self._heapify(idx, len(self.h))

    # Sorts h
    def heapSort(self):
        for i in range(1, len(self.h)):
            self.h[1], self.h[-i] = self.h[-i], self.h[1]
            self._heapify(1, len(self.h) - i - 1)

    def __repr__(self):
        a, *b = self.h
        return '[' + ', '.join(map(str,b)) + ']'

    def __len__(self):
        return len(self.h) - 1
