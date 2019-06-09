from random import randint
import pygal


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)


if __name__ == '__main__':
    dice_a = Dice()
    dice_b = Dice()

    times = 10000
    results = []
    for i in range(times):
        results.append(dice_a.roll() * dice_b.roll())

    frequencies = []
    possible_results = set([a*b for a in range(1, dice_a.sides+1)
                            for b in range(1, dice_b.sides+1)])
    possible_results = sorted(list(possible_results))
    for num in possible_results:
        frequency = results.count(num)
        frequencies.append(frequency)

    histogram = pygal.Bar()
    histogram.title = "Result of rolling two D6 " + str(times) + " times"
    histogram.x_labels = possible_results
    histogram.x_title = "Result"
    histogram.y_title = "Frequency of Result"

    histogram.add("D6 * D6", frequencies)
    histogram.render_to_file("dice_visual.svg")
