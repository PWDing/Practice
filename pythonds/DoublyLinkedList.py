from DoubleNode import DoubleNode


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current = self.head
        data_list = []
        while current is not None:
            data_list.append(str(current.get_data()))
            current = current.get_next()
        return '[' + ', '.join(data_list) + ']'

    def is_empty(self):
        return self.length == 0

    def add(self, item):
        temp = DoubleNode(item)
        temp.set_next(self.head)
        if self.is_empty():
            self.tail = temp
        self.head = temp
        self.length += 1

    def append(self, item):
        temp = DoubleNode(item)
        last = self.tail
        if self.is_empty():
            self.head = temp
        else:
            last.set_next(temp)
        self.tail = temp
        self.tail.set_back(last)
        self.length += 1

    def pop(self, index=None):
        if index is None:
            index = self.length - 1

        if index >= self.length:
            return False
        else:
            count = 0
            previous = None
            current = self.head
            while count < index:
                count += 1
                previous = current
                current = current.get_next()
            new_next = current.get_next()
            if previous is None:
                self.head = new_next
            elif new_next is None:
                self.tail = self.tail.get_back()
                self.tail.set_next(None)
            else:
                previous.set_next(new_next)
                new_next.set_back(previous)
            self.length -= 1


if __name__ == '__main__':
    mylist = DoublyLinkedList()
    mylist.add(6)
    mylist.add(5)
    mylist.append(7)
    mylist.append(8)
    print(mylist.length)
    mylist.pop()
    mylist.pop(4)
    print(mylist)
