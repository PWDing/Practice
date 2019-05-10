class Stack:
    def __init__(self, alist=None):
        if alist is None:
            self.items = []
        else:
            self.items = alist

    def is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peak(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


new_stack = Stack()
new_stack.push(5)
print(new_stack.peak())
print(new_stack.items)


def reverse_string(string):
    result = Stack()
    for i in range(len(string) - 1, -1, -1):
        result.push(string[i])
    return result


def is_balanced_parentheses(parentheses):
    result = Stack()
    for parenthesis in parentheses:
        if parenthesis in '([{':
            result.push(parenthesis)
        else:
            if result.is_empty():
                return False
            elif '([{'.index(result.pop()) != ')]}'.index(parenthesis):
                return False
    if result.is_empty():
        return True
    else:
        return False


def decimal_to_base(decimal, base):
    digits = '0123456789ABCDEF'
    remainders = Stack()
    while decimal:
        remainders.push(decimal % base)
        decimal //= base
    base_string = ''
    while not remainders.is_empty():
        base_string += digits[remainders.pop()]
    return base_string


print(is_balanced_parentheses('((()))'))
print(is_balanced_parentheses('(()'))
print(is_balanced_parentheses('{{([][])}()}'))
print(is_balanced_parentheses('[{()]'))
print(decimal_to_base(25, 8))
print(decimal_to_base(256, 16))
print(decimal_to_base(26, 26))
