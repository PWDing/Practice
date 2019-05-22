import turtle
import random
from collections import defaultdict

from pythonds.Stack import Stack


def convert_to_base_recursion(integer, base):
    convert_string = '0123456789ABCDEF'
    if integer < base:
        return convert_string[integer]
    else:
        return convert_to_base(integer // base, base) \
               + convert_to_base(integer % base, base)


def convert_to_base(integer, base):
    convert_string = '0123456789ABCDEF'
    digits = Stack()
    while integer > 0:
        if integer < base:
            digits.push(convert_string[integer])
        else:
            digits.push(convert_string[integer % base])
        integer //= base

    result = ''
    while not digits.is_empty():
        result += digits.pop()
    return result


def reverse_str(string):
    if len(string) == 1:
        return string
    else:
        return reverse_str(string[1:]) + string[0]


def is_palindrome(string):
    string = string.lower()
    tokens = ',.?:;-\'"‘’“”'
    str_list = [char for char in string if char not in tokens and char != ' ']
    string = ''.join(str_list)
    if len(string) <= 1:
        return True
    else:
        if string[0] != string[-1]:
            return False
        return is_palindrome(string[1:-1])


def draw_spiral(turtle_obj, line_len):
    if length < 360:
        turtle_obj.forward(length)
        turtle_obj.left(90)
        draw_spiral(turtle_obj, length+5)


def draw_fractal_tree(turtle_obj, branch_len, pensize):
    if branch_len > 5:
        if pensize > 0:
            turtle_obj.pensize(pensize)
        turtle_obj.forward(branch_len)
        angle = random.randrange(15, 45, 5)
        sub_len = random.randrange(10, 20)
        turtle_obj.right(angle)
        draw_fractal_tree(turtle_obj, branch_len-sub_len, pensize-1)
        turtle_obj.left(2*angle)
        draw_fractal_tree(turtle_obj, branch_len-sub_len, pensize-1)
        turtle_obj.right(angle)
        if branch_len < 20:
            turtle_obj.color("green")
        else:
            turtle_obj.color("brown")
        turtle_obj.backward(branch_len)


def draw_sierpinski(pen, points, degree):
    """谢尔宾斯基三角形"""
    colors = ['blue', 'red', 'green', 'white', 'yellow',
              'violet', 'orange']
    draw_triangle(pen, points, colors[degree])
    if degree > 0:
        draw_sierpinski(pen, [points[0],
                              get_mid(points[0], points[1]),
                              get_mid(points[0], points[2])],
                        degree-1)
        draw_sierpinski(pen, [points[1],
                              get_mid(points[1], points[0]),
                              get_mid(points[1], points[2])],
                        degree-1)
        draw_sierpinski(pen, [points[2],
                              get_mid(points[2], points[0]),
                              get_mid(points[2], points[1])],
                        degree-1)


def draw_koch_snowflake(pen, length, degree):
    """科赫雪花"""
    if degree == 0:
        pen.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            draw_koch_snowflake(pen, length/3, degree-1)
            pen.left(angle)


def draw_hilbert_curve(pen, length, degree, angle):
    """希尔伯特曲线"""
    if degree > 0:
        pen.left(angle)
        draw_hilbert_curve(pen, length, degree-1, -angle)
        pen.forward(length)
        pen.right(angle)
        draw_hilbert_curve(pen, length, degree-1, angle)
        pen.forward(length)
        draw_hilbert_curve(pen, length, degree-1, angle)
        pen.right(angle)
        pen.forward(length)
        draw_hilbert_curve(pen, length, degree-1, -angle)
        pen.left(angle)


def get_mid(pos1, pos2):
    return [(pos1[0]+pos2[0])/2, (pos1[1]+pos2[1])/2]


# 获取三等分点
def get_bece(pos1, pos2):
    point1 = [(2*pos1[0]+pos2[0])/3, (2*pos1[1]+pos2[1])/3]
    point2 = [(pos1[0]+2*pos2[0])/3, (pos1[1]+2*pos2[1])/3]
    return [point1, point2]


def draw_triangle(pen, points, color):
    pen.fillcolor(color)
    pen.hideturtle()
    pen.up()
    pen.goto(points[0][0], points[0][1])
    pen.down()
    pen.begin_fill()
    pen.goto(points[1][0], points[1][1])
    pen.goto(points[2][0], points[2][1])
    pen.goto(points[0][0], points[0][1])
    pen.end_fill()


def make_pascal(row):
    if row == 1:
        pascal = [0, 1, 0]
    else:
        temp = make_pascal(row-1)
        pascal = [0]
        pascal.extend([temp[i]+temp[i+1] for i in range(len(temp)-1)])
        pascal.append(0)
    return pascal


def draw_pascal(rows):
    pascals = []
    for row in range(1, rows+1):
        pascal = ' '.join([str(num) for num in make_pascal(row) if num != 0])
        pascals.append(pascal)

    for row in pascals:
        print(row.center(30))


def draw_fractal_mountain(pen, points, degree):
    """用三角形绘制分形山
    """
    colors = ['blue', 'red', 'green', 'pink', 'yellow',
              'violet', 'orange', 'black']
    draw_triangle(pen, points, colors[0])
    floor = 1
    while floor < degree:
        # 算出小三角形的高和底边长
        height = points[1][1] - points[0][1]
        width = points[2][0] - points[0][0]
        for i in range(floor+1):
            # 每层中小三角形的顶点坐标
            new_points = [[points[0][0]-width/2+i*width, points[0][1]-height],
                          [points[0][0]+i*width, points[0][1]],
                          [points[0][0]+width/2+i*width, points[0][1]-height]]
            draw_triangle(pen, new_points, colors[floor])

        floor += 1
        # 计算下一层最左三角形的顶点坐标
        points = [[points[0][0]-width/2, points[0][1]-height],
                  [points[0][0], points[0][1]],
                  [points[0][0]+width/2, points[0][1]-height]]


def hanoi(n, from_rod, aux_rod, to_rod):
    if n >= 1:
        hanoi(n-1, from_rod, to_rod, aux_rod)
        print("move top disk from {} to {}.".format(from_rod, to_rod))
        hanoi(n-1, aux_rod, from_rod, to_rod)


def make_change(change, known_result):
    cointypes = [25, 21, 10, 5, 1]
    min_coins = change
    if change in cointypes:
        known_result[change] = 1
        return 1
    elif known_result[change] > 0:
        return known_result[change]
    else:
        for n in [coin for coin in cointypes if coin <= change]:
            coin_nums = 1 + make_change((change-n), known_result)
            if coin_nums < min_coins:
                min_coins = coin_nums
                known_result[change] = min_coins
    return min_coins


# bag表示背包容量，wts表示每个物品占据的空间组成的列表
# vals表示每个物品的价值，顺序和其占据空间是一致的
# num表示物品数量
# 直接debug可以得到正确结果，ctrl+F5不打印任何值(不知道是什么原因)
def knapsack(bag, wts, vals, num):
    if bag == 0 or num == 0:
        return 0

    if wts[num-1] > bag:
        return knapsack(bag, wts, vals, num-1)
    else:
        return max(vals[num-1]+knapsack(bag-wts[num-1], wts, vals, num-1),
                   knapsack(bag, wts, vals, num-1))


# This function is used to initialize the
# dictionary elements with a default value.
# jug1 and jug2 contain the value
# for max capacity in respective jugs
# and aim is the amount of water to be measured.
jug1, jug2, aim = 4, 3, 2

# Initialize dictionary with
# default value as false.
visited = defaultdict(lambda: False)


# Recursive function which prints the
# intermediate steps to reach the final
# solution and return boolean value
# (True if solution is possible, otherwise False).
# amt1 and amt2 are the amount of water present
# in both jugs at a certain point of time.
def water_jugs(amt1, amt2):

    # Checks for our goal and
    # returns true if achieved.
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        if jug1 < jug2:
            print(amt1, amt2)
        else:
            print(amt2, amt1)
        return True

    # Checks if we have already visited the
    # combination or not. If not, then it proceeds further.
    if not visited[(amt1, amt2)]:
        print(amt1, amt2)

        # Changes the boolean value of
        # the combination as it is visited.
        visited[(amt1, amt2)] = True

        # Check for all the 6 possibilities and
        # see if a solution is found in any one of them.
        return (water_jugs(0, amt2) or
                water_jugs(amt1, 0) or
                water_jugs(jug1, amt2) or
                water_jugs(amt1, jug2) or
                water_jugs(amt1 + min(amt2, (jug1-amt1)),
                amt2 - min(amt2, (jug1-amt1))) or
                water_jugs(amt1 - min(amt1, (jug2-amt2)),
                amt2 + min(amt1, (jug2-amt2))))

    # Return False if the combination is
    # already visited to avoid repetition otherwise
    # recursion will enter an infinite loop.
    else:
        return False


# 食人魔和传教士人数相同时，可解决的问题规模最大为3
def cross_river(number):
    print("Two cannibal cross the river by boat.")
    print("One cannibal get back from other bank.")
    print("One missionary and one cannibal cross the river by boat.")
    print("One cannibal get back from other bank.")
    print("Two missionaries cross the river by boat.")
    print("One cannibal get back from other bank.")
    print("Two cannibal cross the river by boat.")
    print("One cannibal get back from other bank.")
    print("Two cannibal cross the river by boat.")


def factorial(number):
    if number < 2:
        return 1
    else:
        return number * factorial(number-1)


# 一行代码搞定反转列表
# return alist[-1::-1]
def reverse_list(alist):
    size = len(alist)
    mid = size // 2
    for i in range(mid):
        alist[i], alist[size-1-i] = alist[size-1-i], alist[i]
    return alist


if __name__ == '__main__':
    # print(convert_to_base(256, 16))
    # print(convert_to_base(1453, 16))

    # print(reverse_str('pluto'))

    # print(is_palindrome('radar'))
    # print(is_palindrome('aibohphobia'))
    # print(is_palindrome('Live not on evil'))
    # print(is_palindrome('Reviled did I live, said I, as evil I did deliver'))
    # print(is_palindrome('Go hang a salami; I’m a lasagna hog.'))
    # print(is_palindrome('Able was I ere I saw Elba'))
    # print(is_palindrome('Kanakanak – a town in Alaska'))
    # print(is_palindrome('Wassamassaw – a town in South Dakota'))

    my_pen = turtle.Turtle()
    my_pen.shape('turtle')
    # my_screen = turtle.Screen()
    # draw_spiral(my_pen, 10)
    # my_pen.left(90)
    # my_pen.up()
    # my_pen.backward(100)
    # my_pen.down()
    # my_pen.color("brown")
    # draw_fractal_tree(my_pen, 75, 5)

    # my_points = [[-100, -50], [0, 100], [100, -50]]
    # draw_sierpinski(my_pen, my_points, 5)

    # my_pen.color('white')
    # my_pen.goto(-300, 200)
    # my_pen.color('blue')
    # for i in range(3):
    #     draw_koch_snowflake(my_pen, 300, 3)
    #     my_pen.right(120)

    my_pen.color('white')
    my_pen.goto(-200, -200)
    my_pen.color('blue')
    draw_hilbert_curve(my_pen, 10, 5, 90)

    # mountain_points = [[-20, -10], [0, 10], [20, -10]]
    # draw_fractal_mountain(my_pen, mountain_points, 7)

    # my_screen.exitonclick()

    # hanoi(4, 'A', 'B', 'C')

    # print(make_change(63, [0]*64))

    # my_list = ['a', 'b', 'c', 'd']
    # reverse_list(my_list)
    # print(my_list)

    # cross_river(3)

    # water_jugs(0, 0)

    # draw_pascal(10)

    # bag = 20
    # weights = [2, 3, 4, 5, 9]
    # values = [3, 4, 8, 8, 10]
    # number = len(values)
    # print(knapsack(bag, weights, values, number))
