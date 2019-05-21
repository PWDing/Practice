import turtle
import random

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


def get_mid(pos1, pos2):
    return [(pos1[0]+pos2[0])/2, (pos1[1]+pos2[1])/2]


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


def hanoi(n, from_rod, aux_rod, to_rod):
    if n >= 1:
        hanoi(n-1, from_rod, to_rod, aux_rod)
        print("move top disk from {} to {}.".format(from_rod, to_rod))
        hanoi(n-1, aux_rod, from_rod, to_rod)


def make_change(change, known_result):
    cointypes = [25, 10, 5, 1]
    min_coins = change
    if change in cointypes:
        known_result[change] = 1
        return 1
    elif known_result[change] > 0:
        return known_result[change]
    else:
        for n in [coin for coin in cointypes if coin < change]:
            coin_nums = 1 + make_change((change-n), known_result)
            if coin_nums < min_coins:
                min_coins = coin_nums
                known_result[change] = min_coins
    return min_coins


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

    # my_pen = turtle.Turtle()
    # my_screen = turtle.Screen()
    # draw_spiral(my_pen, 10)
    # my_pen.left(90)
    # my_pen.up()
    # my_pen.backward(100)
    # my_pen.down()
    # my_pen.color("brown")
    # draw_fractal_tree(my_pen, 75, 5)
    # my_screen.exitonclick()

    # my_points = [[-100, -50], [0, 100], [100, -50]]
    # draw_sierpinski(my_pen, my_points, 5)

    # hanoi(4, 'A', 'B', 'C')

    print(make_change(20, [0]*21))
