import random


class Queue:

    def __init__(self, alist=None):
        if alist is None:
            self.items = []
        else:
            self.items = alist[:]

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)
        return self.items

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)


def hot_potato(alist):
    num = random.randrange(2, 7)
    alist.reverse()
    game_queue = Queue(alist)
    while game_queue.size() > 1:
        # 前 num-1 个玩家每次从队尾出队又从队首入队
        for i in range(num-1):
            game_queue.enqueue(game_queue.dequeue())
        # 第 num 个玩家被淘汰 
        game_queue.dequeue()
    return game_queue.dequeue()


def radix_sort(alist, base):
    if alist is None:
        return None

    digit = 1
    size = len(alist)
    maximum = max(alist)
    max_digits = maximum
    main_bin = Queue(alist)
    while max_digits > 0:
        digits = [[] for n in range(base)]
        for i in range(size):
            pending = main_bin.dequeue()
            quotient = pending // digit
            digits[quotient % base].append(pending)
        for j in range(base):
            for k in range(len(digits[j])):
                main_bin.enqueue(digits[j][k])
        digit *= base
        max_digits //= base
    return main_bin


if __name__ == '__main__':
    players = ['ame', 'maybe', 'chalice', 'fy', 'xnova', 'pluto']
    print(hot_potato(players))
    
    numbers = [256, 230, 890, 257, 122, 365, 1000]
    result = radix_sort(numbers, 10)
    while not result.is_empty():
        print(result.dequeue())
