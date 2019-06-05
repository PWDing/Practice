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

    def get_min_child(self, pos):
        if self.items[2*pos] < self.items[2*pos+1]:
            return 2 * pos
        else:
            return 2 * pos + 1

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
        return minimum


if __name__ == '__main__':
    test = BinHeap()
    test.insert(8)
    test.insert(9)
    test.insert(3)
    for item in test.items:
        print(item)
