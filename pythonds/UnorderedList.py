from Node import Node


class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current = self.head
        unordered_list = []
        while current is not None:
            unordered_list.append(str(current.get_data()))
            current = current.get_next()
        return '[' + ', '.join(unordered_list) + ']'

    def is_empty(self):
        return self.length == 0

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        if self.is_empty():
            self.tail = temp
        self.head = temp
        self.length += 1

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.get_next()
        return False

    def pop(self, index=None):
        if index is None:
            index = self.length - 1
        if self.length > index:
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
            self.length -= 1
            return current.get_data()

    def remove(self, item):
        found = False
        previous = None
        current = self.head
        while current is not None and not found:
            if current.get_data() == item:
                found = True
                self.length -= 1
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
        temp = Node(item)
        last = self.tail
        if self.is_empty():
            self.head = temp
        else:
            last.set_next(temp)
        self.tail = temp
        self.length += 1

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
        if self.length >= index:
            temp = Node(item)
            count = 0
            previous = None
            current = self.head
            while count < index:
                previous = current
                current = current.get_next()
                count += 1
            temp.set_next(current)
            if index:
                previous.set_next(temp)
            else:
                self.head = temp
            self.length += 1


if __name__ == '__main__':
    mylist = UnorderedList()
    mylist.append(0)
    print(mylist)
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
    print(mylist.length)
    print(mylist)
