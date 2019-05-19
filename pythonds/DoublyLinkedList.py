from DoubleNode import DoubleNode


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        # self.tail = None
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
        if self.is_empty():
            # 若链表为空，则新节点的back指针指向自身
            temp.set_back(temp)
        else:
            # 新节点的back指针指向尾节点
            temp.set_back(self.head.get_back())
            # 新节点的next指针指向原来的头节点
            temp.set_next(self.head)
            # 使原来的头节点的back指针指向新节点
            self.head.set_back(temp)
        # 将新节点设为头节点
        self.head = temp
        self.length += 1

    def append(self, item):
        temp = DoubleNode(item)
        if self.is_empty():
            temp.set_back(temp)
            self.head = temp
        else:
            # 获取原来的尾节点
            last = self.head.get_back()
            # 更新原来的尾节点的next指针
            last.set_next(temp)
            # 设置新节点的back指针为原来的尾节点
            temp.set_back(last)
            # 更新头节点的back指针
            self.head.set_back(temp)
        self.length += 1

    def pop(self, index=None):
        # 忽略参数，则弹出链表的最后一项
        if index is None:
            index = self.length - 1

        if index >= self.length:
            return False
        else:
            previous = None
            current = self.head
            while index > 0:
                index -= 1
                previous = current
                current = current.get_next()
            new_next = current.get_next()
            # 若previous为None，则说明弹出的是第一项
            if previous is None:
                # 更新原来的第二项的back指针
                new_next.set_back = self.head.get_back()
                # 更新头节点
                self.head = new_next
            # 若当前节点的下一个节点为None，则说明弹出的是最后一项
            elif new_next is None:
                # 获取原来的尾节点
                last = self.head.get_back()
                # 更新原来的倒数第二项的next指针
                last.get_back().set_next(None)
                # 更新头节点的back指针，使其指向原来的倒数第二项
                self.head.set_back(last.get_back())
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
    mylist.append(9)
    mylist.pop(3)
    print(mylist)
