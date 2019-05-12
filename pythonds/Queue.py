class Queue:

    def __init__(self, alist=None):
        if alist is None:
            self.items = []
        else:
            self.items = alist

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
        return self.items

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def size(self):
        return len(self.items)


def hot_potato(alist, num):
    alist.reverse()
    game_queue = Queue(alist)
    while game_queue.size() > 1:
        for i in range(num-1):
            game_queue.enqueue(game_queue.dequeue())
        game_queue.dequeue()
    return game_queue.dequeue()


if __name__ == '__main__':
    players = ['ame', 'maybe', 'chalice', 'fy', 'xnova', 'pluto']
    print(hot_potato(players, 5))
