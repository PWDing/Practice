class Stack:
    def __init__(self, alist=None):
        if alist is None:
            self.items = []
        else:
            self.items = alist

    def isEmpty(self):
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


def revstring(mystr):
    result = Stack()
    for i in range(len(mystr) - 1, -1, -1):
        result.push(mystr[i])
    return result


def is_balanced_parentheses(parentheses):
    result = Stack()
    for parenthesis in parentheses:
        if parenthesis in '([{':
            result.push(parenthesis)
        else:
            if result.isEmpty():
                return False
            elif '([{'.index(result.pop()) != ')]}'.index(parenthesis):
                return False
    if result.isEmpty():
        return True
    else:
        return False


print(is_balanced_parentheses('((()))'))
print(is_balanced_parentheses('(()'))
print(is_balanced_parentheses('{{([][])}()}'))
print(is_balanced_parentheses('[{()]'))
