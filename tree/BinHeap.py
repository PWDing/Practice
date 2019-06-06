class BinHeap:
    def __init__(self):
        self.items = [0]
        self.size = 0

    def percolate_up(self, pos):
        while pos > 0:
            parent = pos // 2
            if self.items[pos] < self.items[parent]:
                self.items[parent], self.items[pos] = \
                    self.items[pos], self.items[parent]
                pos //= 2
            else:
                break

    def percolate_down(self, pos):
        while 2 * pos <= self.size:
            min_child_idx = self.get_min_child(pos)
            if self.items[pos] > self.items[min_child_idx]:
                self.items[pos], self.items[min_child_idx] = \
                    self.items[min_child_idx], self.items[pos]
            pos = min_child_idx

    def get_min_child(self, pos):
        lchild = 2 * pos
        rchild = 2 * pos + 1
        if rchild > self.size:
            return lchild
        else:
            if self.items[lchild] < self.items[rchild]:
                return lchild
            else:
                return rchild

    def insert(self, new_added):
        self.items.append(new_added)
        self.size += 1
        self.percolate_up(self.size)

    def del_min(self):
        if self.size < 1:
            return False
        minimum = self.items[1]
        self.items[1] = self.items[self.size]
        self.size -= 1
        self.items.pop()
        self.percolate_down(1)
        return minimum

    def build_heap(self, alist):
        self.items.extend(alist[:])
        self.size += len(alist)
        index = self.size // 2
        while index > 0:
            self.percolate_down(index)
            index -= 1


if __name__ == '__main__':
    test = BinHeap()
    test.insert(8)
    test.insert(9)
    test.insert(3)
    test.del_min()
    test.build_heap([4, 6, 2, 1])
    print(test.del_min())
    print(test.del_min())
    print(test.del_min())
    print(test.del_min())
    print(test.del_min())
    print(test.del_min())
    print(test.del_min())
    for item in test.items:
        print(item)
