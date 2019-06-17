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


def preorder(atree):
    if atree:
        print(atree.get_root())
        preorder(atree.get_left_child())
        preorder(atree.get_right_child())


def inorder(atree):
    infix_exp = ''
    if atree:
        infix_exp = '(' + inorder(atree.get_left_child())
        infix_exp += str(atree.get_root())
        infix_exp += inorder(atree.get_right_child()) + ')'
    return infix_exp


def eliminate(string):
    tolist = list(string)
    for i in range(len(tolist)):
        if tolist[i-1] == '(' and tolist[i+1] == ')':
            tolist[i-1] = ' '
            tolist[i+1] = ' '
    new_list = [char for char in tolist if char != ' ']
    infix = ''
    for item in new_list:
        infix += item
    return infix


def postorder(atree):
    if atree:
        postorder(atree.get_left_child())
        postorder(atree.get_right_child())
        print(atree.get_root())


def postorder_evaluate(atree):
    left_result = None
    right_result = None
    if atree:
        left_result = postorder_evaluate(atree.get_left_child())
        right_result = postorder_evaluate(atree.get_right_child())
        if left_result and right_result:
            return calculate(left_result, right_result, atree.get_root())
        else:
            return atree.get_root()


if __name__ == '__main__':
    # test_exp = '( 3 * ( 4 + 5 ) )'
    test_exp = '( ( ( 4 * 8 ) / 6 ) - 3 )'
    result = parse_tree(test_exp)
    # preorder(result)
    print(eliminate(inorder(result)))
    postorder(result)
    # print(evaluate(result))
    # print(postorder_evaluate(result))
