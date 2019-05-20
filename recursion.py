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


def draw_fractal_tree(branch_len, turtle_obj, pensize):
    if branch_len > 5:
        if pensize > 0:
            turtle_obj.pensize(pensize)
        turtle_obj.forward(branch_len)
        angle = random.randrange(15, 45, 5)
        sub_len = random.randrange(10, 20)
        turtle_obj.right(angle)
        draw_fractal_tree(branch_len-sub_len, turtle_obj, pensize-1)
        turtle_obj.left(2*angle)
        draw_fractal_tree(branch_len-sub_len, turtle_obj, pensize-1)
        turtle_obj.right(angle)
        if branch_len < 20:
            turtle_obj.color("green")
        else:
            turtle_obj.color("brown")
        turtle_obj.backward(branch_len)


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

    my_turtle = turtle.Turtle()
    my_screen = turtle.Screen()
    # draw_spiral(my_turtle, 10)
    my_turtle.left(90)
    my_turtle.up()
    my_turtle.backward(100)
    my_turtle.down()
    my_turtle.color("brown")
    draw_fractal_tree(75, my_turtle, 5)
    my_screen.exitonclick()
