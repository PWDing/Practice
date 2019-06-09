import matplotlib.pyplot as plt


def draw_plot():
    values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    plt.plot(values, squares, linewidth=5)

    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    plt.tick_params(axis="both", labelsize=14)
    plt.show()


def draw_scatter():
    values = list(range(1, 1001))
    squares = [num**2 for num in values]
    plt.scatter(values, squares, c=squares, cmap=plt.cm.Blues,
                edgecolors="None", s=20)
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    plt.axis([0, 1100, 0, 1100000])
    plt.tick_params(axis="both", which="major", labelsize=14)
    plt.show()
    # plt.savefig("squares_plot.png", bbox_inches="tight")


if __name__ == '__main__':
    draw_scatter()
