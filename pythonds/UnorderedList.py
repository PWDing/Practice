import Node


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node.Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        found = False
        previous = None
        current = self.head
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            return False
        elif previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        return True


if __name__ == '__main__':
    mylist = UnorderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    print(mylist.size())
    print(mylist.search(17))
    print(mylist.remove(54))
    print(mylist.search(54))
    print(mylist.remove(20))
