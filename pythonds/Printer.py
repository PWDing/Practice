import random

from Queue import Queue


class Printer:
    def __init__(self, pages_per_minute):
        self.pages_per_minute = pages_per_minute
        self.current_task = None
        self.time_remaining = 0

    def busy(self):
        if self.current_task is None:
            return False
        return True

    def tick(self):
        if self.current_task is not None:
            # 因为调用该函数的地方在一个循环语句中，该循环步长为 1s，所以每次减一
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def start_next_task(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.pages_per_minute


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_pages(self):
        return self.pages

    def get_timestamp(self):
        return self.timestamp

    def wait_time(self, current_time):
        return current_time - self.timestamp


def simulate_print(total_seconds, pages_per_minute):
    printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(total_seconds):
        if arise_new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if not printer.busy() and not print_queue.is_empty():
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            printer.start_next_task(next_task)

        printer.tick()

    average_waiting_time = sum(waiting_times) / len(waiting_times)
    print("Average wait %6.2f seconds," % average_waiting_time, end="")
    print("There is %2d tasks remaining." % print_queue.size())


# 不一定非得等于 180，其实 1~180 中任何一个数都可以，因为每个数出现的几率都是 1/180
# 那么调用这个函数 180 次恰好会出现一次 180，也就是平均每 180s 会产生一个打印任务
def arise_new_print_task():
    if random.randrange(1, 181) == 180:
        return True
    return False


if __name__ == '__main__':
    for i in range(10):
        simulate_print(3600, 5)
