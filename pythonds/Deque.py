class Deque:
    def __init__(self, alist=None):
        if len(alist) is None:
            self.items = []
        else:
            self.items = alist

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def del_front(self):
        if not self.is_empty():
            return self.items.pop(0)

    def del_rear(self):
        if not self.is_empty():
            return self.items.pop()


def check_palindrome(string):
    pending = Deque(list(string))
    while pending.size() > 1:
        if pending.del_front() != pending.del_rear():
            return False
    return True


if __name__ == '__main__':
    string1 = 'radars'
    string2 = 'toot'
    print(check_palindrome(string1))
    print(check_palindrome(string2))
