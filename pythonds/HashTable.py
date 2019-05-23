class HashTable:
    def __init__(self, size=None):
        if size is None:
            self.size = 11
        else:
            self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def put(self, key, value):
        slot_idx = self.hash_func(key)
        if self.slots[slot_idx] is None:
            self.slots[slot_idx] = key
            self.data[slot_idx] = value
        else:
            if self.slots[slot_idx] == key:
                self.data[slot_idx] = value
            else:
                next_slot = self.rehash(slot_idx)
                while self.slots[next_slot] is not None\
                        and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot)
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = value
                else:
                    self.data[next_slot] = value

    def get(self, key):
        start_slot = self.hash_func(key)

        data = None
        stop = False
        found = False
        pos = start_slot
        while self.slots[pos] is not None and\
                not found and not stop:
            if self.slots[pos] == key:
                found = True
                data = self.data[pos]
            else:
                pos = self.rehash(pos)
                if pos == start_slot:
                    stop = True
        return data

    def hash_func(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash+1) % self.size


if __name__ == '__main__':
    my_hash = HashTable()
    my_hash[54] = "cat"
    my_hash[26] = "dog"
    my_hash[93] = "lion"
    my_hash[17] = "tiger"
    my_hash[77] = "bird"
    my_hash[31] = "cow"
    my_hash[44] = "goat"
    my_hash[55] = "pig"
    my_hash[20] = "chicken"
    print(my_hash.slots)
    print(my_hash.data)
