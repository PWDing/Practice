import OutsidePackage
import BinaryTree
from pythonds.Stack import Stack
from pythonds.Stack import calculate


def parse_tree(math_exp):
    exp_list = math_exp.split(' ')
    operators = '+-*/'
    temp_stack = Stack()
    exp_tree = BinaryTree.BinaryTree('')
    temp_stack.push(exp_tree)
    current = exp_tree
    for token in exp_list:
        if token == '(':
            current.insert_left('')
            temp_stack.push(current)
            current = current.get_left_child()
        elif token in operators:
            current.set_root(token)
            current.insert_right('')
            temp_stack.push(current)
            current = current.get_right_child()
        elif token == ')':
            current = temp_stack.pop()
        elif token not in operators:
            try:
                current.set_root(int(token))
                parent = temp_stack.pop()
                current = parent
            except ValueError:
                raise ValueError("'{}' is not a valid integer".format(token))
    return exp_tree


def evaluate(parse_tree):
    left_tree = parse_tree.get_left_child()
    right_tree = parse_tree.get_right_child()
    if left_tree and right_tree:
        operator = parse_tree.get_root()
        return calculate(evaluate(left_tree), evaluate(right_tree), operator)
    else:
        return parse_tree.get_root()


if __name__ == '__main__':
    test_exp = '( 3 * ( 4 + 5 ) )'
    print(parse_tree(test_exp))
    print(evaluate(parse_tree(test_exp)))
