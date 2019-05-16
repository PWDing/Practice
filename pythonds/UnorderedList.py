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

    def pop(self, index=0):
        if self.size() > index:
            count = 0
            previous = None
            current = self.head
            while count < index:
                count += 1
                previous = current
                current = current.get_next()
            if previous:
                previous.set_next(current.get_next())
            else:
                self.head = current.get_next()
            return current.get_data()

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
        return found

    def append(self, item):
        new_node = Node.Node(item)
        current = self.head
        if current:
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
        else:
            self.head = new_node

    def index(self, item):
        index = 0
        current = self.head
        while current:
            if current.get_data() != item:
                index += 1
                current = current.get_next()
            else:
                return index

    def insert(self, index, item):
        if self.size() >= index:
            new_node = Node.Node(item)
            count = 0
            previous = None
            current = self.head
            while count < index:
                previous = current
                current = current.get_next()
                count += 1
            new_node.set_next(current)
            if index:
                previous.set_next(new_node)
            else:
                self.head = new_node


if __name__ == '__main__':
    mylist = UnorderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    mylist.append(20)
    mylist.append(9)
    print(mylist.index(54))
    print(mylist.index(9))
    mylist.insert(0, 8)
    mylist.insert(9, 5)
    print(mylist.index(8))
    print(mylist.index(5))
    print(mylist.pop())
    print(mylist.pop(8))
    current = mylist.head
    while current:
        print(current.get_data())
        current = current.get_next()
