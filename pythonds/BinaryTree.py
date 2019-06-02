class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            new_tree = BinaryTree(new_node)
            new_tree.left_child = self.left_child
            self.left_child = new_tree

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            new_tree = BinaryTree(new_node)
            new_tree.right_child = self.right_child
            self.right_child = new_tree

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root(self, obj):
        self.root = obj

    def get_root(self):
        return self.root


if __name__ == '__main__':
    r = BinaryTree('a')
    print(r.get_root())
    print(r.get_left_child())
    r.insert_left('b')
    print(r.get_left_child())
    print(r.get_left_child().get_root())
    r.insert_right('c')
    print(r.get_right_child())
    print(r.get_right_child().get_root())
    r.get_right_child().set_root('hello')
    print(r.get_right_child().get_root())
