from random import choice
import matplotlib.pyplot as plt


class RandomWalk:
    def __init__(self, point_nums=5000):
        self.point_nums = point_nums

        # all walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.point_nums:
            x_step = self.get_steps()
            y_step = self.get_steps()

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_steps(self):
        direction = choice([-1, 1])
        distance = choice(list(range(8)))
        return direction * distance


if __name__ == '__main__':
    point_numbers = 10000
    color_numbers = list(range(10000))
    my_walks = RandomWalk(point_numbers)
    my_walks.fill_walk()

    # set the size of the plotting window
    plt.figure(dpi=128, figsize=(16, 9))

    # plt.plot(my_walks.x_values, my_walks.y_values, linewidth=1)

    plt.scatter(my_walks.x_values, my_walks.y_values,
                c=color_numbers, cmap=plt.cm.Blues, s=1)

    # Emphasize the first and last points
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(my_walks.x_values[-1], my_walks.y_values[-1], c='red', s=100)

    # Cleaning up the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
