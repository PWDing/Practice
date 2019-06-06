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
        left_child = 2 * pos
        right_child = 2 * pos + 1
        if right_child > self.size:
            return left_child
        else:
            if self.items[left_child] < self.items[right_child]:
                return left_child
            else:
                return right_child

    def insert(self, new_added):
        self.items.append(new_added)
        self.size += 1
        self.percolate_up(self.size)

    def del_min(self):
        if self.size < 1:
            return False
        minimum = self.items[1]
        self.items[1] = self.items.pop()
        self.size -= 1
        self.percolate_down(1)
        return minimum


if __name__ == '__main__':
    test = BinHeap()
    test.insert(8)
    test.insert(9)
    test.insert(3)
    test.del_min()
    for item in test.items:
        print(item)
