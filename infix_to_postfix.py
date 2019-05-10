def infix_to_postfix(infix):
    precedence = {
        '(': 0,
        ')': 0,
        '*': 1,
        '/': 1,
        '+': 2,
        '-': 2,
    }
    opstack = []
    postfix = []
    for char in infix.split(' '):
        opstack_size = len(opstack)
        if char in precedence.keys():
            if opstack_size != 0:
                if char == ')':
                    top_operator = opstack.pop()
                    while top_operator != '(':
                        postfix.append(top_operator)
                        top_operator = opstack.pop()
                elif precedence[char] >= precedence[opstack[-1]] and opstack[-1] != '(':
                    postfix.append(opstack.pop())
                    opstack.append(char)
                else:
                    opstack.append(char)
            else:
                opstack.append(char)
        else:
            postfix.append(char)

    while len(opstack) != 0:
        postfix.append(opstack.pop())
    postfix_expression = ' '.join(postfix)
    return postfix_expression


def calculate_postfix(postfix):
    operators = '+-*/'
    operands = []
    for char in postfix.split(' '):
        if char in operators:
            right_operand = operands.pop()
            left_operand = operands.pop()
            new_top_operand = calculate(int(left_operand), int(right_operand), char)
            operands.append(new_top_operand)
        else:
            operands.append(char)
    return operands[0]


def calculate(num1, num2, operator):
    result = 0
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    return result


a = '( A + B ) * ( C + D )'
b = '( A + B ) * C - ( D - E ) * ( F + G )'
c = '( ( A + B ) + C ) * D'
d = 'A + B * C'
e = '12 20 + 3 *'
f = '7 8 + 3 2 + /'
# print(infix_to_postfix(a))
# print(infix_to_postfix(b))
# print(infix_to_postfix(c))
# print(infix_to_postfix(d))
print(calculate_postfix(e))
print(calculate_postfix(f))
