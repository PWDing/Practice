from Node import Node


class OrderedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def add(self, item):
        stop = False
        previous = None
        current = self.head
        while current is not None and not stop:
            if current.get_data() < item:
                previous = current
                current = current.get_next()
            else:
                stop = True

        temp = Node(item)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
        self.length += 1

    def search(self, item):
        stop = False
        found = False
        current = self.head
        while current is not None and not found and not stop:
            current_data = current.get_data()
            if current_data == item:
                found = True
            elif current_data > item:
                stop = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        found = False
        previous = None
        current = self.head
        while current is not None and not found:
            if current.get_data() == item:
                found = True
                self.length -= 1
            elif current.get_data() > item:
                return False
            else:
                previous = current
                current = current.get_next()

        if current is None:
            return False
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def index(self, item):
        stop = None
        index = 0
        current = self.head
        while current is not None and current.get_data() != item and not stop:
            if current.get_data() > item:
                stop = True
            else:
                current = current.get_next()
                index += 1
        if current is None or current.get_data() != item:
            return False
        else:
            return index

    def pop(self, index=None):
        if index is None:
            index = self.length - 1
        if self.length > index:
            count = 0
            previous = None
            current = self.head
            while count < index:
                previous = current
                current = current.get_next()
                count += 1
            if previous is None:
                self.head = current.get_next()
                return current.get_data()
            else:
                previous.set_next(current.get_next())
                return current.get_data()
        else:
            return False


if __name__ == '__main__':
    ordered = OrderedList()
    ordered.add(5)
    ordered.add(8)
    ordered.add(6)
    print(ordered.search(5))
    print(ordered.search(7))
    print(ordered.remove(9))
    print(ordered.index(5))
    print(ordered.pop(1))
    current = ordered.head
    while current:
        print(current.get_data())
        current = current.get_next()
