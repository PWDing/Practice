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
        if not self.is_empty():
            return self.items.pop()

    def peak(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


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


def infix_to_postfix(infix):
    operators = {
        '(': 0,
        ')': 0,
        '*': 1,
        '/': 1,
        '+': 2,
        '-': 2,
    }
    postfix = []
    opstack = Stack()
    infix_list = infix.split(' ')
    for item in infix_list:
        if item not in operators.keys():
            postfix.append(item)
        else:
            if item == ')':
                top_operator = opstack.pop()
                while top_operator and top_operator != '(':
                    postfix.append(top_operator)
                    top_operator = opstack.pop()
            else:
                if not opstack.is_empty() and \
                        opstack.peak() != '(' and \
                        operators[item] >= operators[opstack.peak()]:
                    postfix.append(opstack.pop())
                opstack.push(item)
    while not opstack.is_empty():
        postfix.append(opstack.pop())
    postfix_expression = ' '.join(postfix)
    return postfix_expression


def calculate_postfix(postfix):
    operators = '*/+-'
    operands = Stack()
    start = 0
    for i in range(len(postfix)):
        if postfix[i] in operators:
            right_operand = int(operands.pop())
            left_operand = int(operands.pop())
            operands.push(calculate(left_operand, right_operand, postfix[i]))
            start = i + 1
        elif postfix[i] == ' ' and postfix[start:i] not in operators:
            operands.push(postfix[start:i])
            start = i + 1
    return operands.pop()


def calculate(operand1, operand2, operator):
    result = None
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/' and operand2 != 0:
        result = operand1 / operand2
    return result


if __name__ == '__main__':
    # print(is_balanced_parentheses('((()))'))
    # print(is_balanced_parentheses('(()'))
    # print(is_balanced_parentheses('{{([][])}()}'))
    # print(is_balanced_parentheses('[{()]'))
    # print(decimal_to_base(25, 8))
    # print(decimal_to_base(256, 16))
    # print(decimal_to_base(26, 26))
    # a = 'A * ( ( B + C ) / D )'
    # b = '3 * ( ( 4 + 6 ) / 5 )'
    # c = '25 + ( 12 + 15 ) / ( 3 * 3 )'
    d = '( A + B ) * ( C + D ) * ( E + F )'
    e = 'A + ( ( B + C ) * ( D + E ) )'
    f = 'A * B * C * D + E + F'
    g = '2 3 * 4 +'
    h = '1 2 + 3 + 4 + 5 +'
    i = '1 2 3 4 5 * + * +'
    # print(infix_to_postfix(a))
    # print(calculate_postfix(infix_to_postfix(b)))
    # print(calculate_postfix(infix_to_postfix(c)))
    print(infix_to_postfix(d))
    print(infix_to_postfix(e))
    print(infix_to_postfix(f))
    print(calculate_postfix(g))
    print(calculate_postfix(h))
    print(calculate_postfix(i))
