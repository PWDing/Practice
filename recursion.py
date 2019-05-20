def convert_to_base(integer, base):
    convert_string = '0123456789ABCDEF'
    if integer < base:
        return convert_string[integer]
    else:
        return convert_to_base(integer // base, base) \
               + convert_to_base(integer % base, base)


def reverse_str(string):
    if len(string) == 1:
        return string
    else:
        return reverse_str(string[1:]) + string[0]


def check_palindrome(string):
    # tokens = ',.?:;'
    size = len(string)
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]:
            check_palindrome(string[1:-1])
        return False


if __name__ == '__main__':
    print(convert_to_base(256, 16))
    print(reverse_str('pluto'))
    print(check_palindrome('radar'))
