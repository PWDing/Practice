class BinSearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _put(self, key, value, current):
        if key < current.key:
            if current.has_left_child():
                self._put(key, value, current.lchild)
            else:
                current.lchild = TreeNode(key, value, parent=current)
        else:
            if current.has_right_child():
                self._put(key, value, current.rchild)
            else:
                current.rchild = TreeNode(key, value, parent=current)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.value

    def _get(self, key, current):
        if not current:
            return None
        elif key == current.key:
            return current
        elif key < current.key:
            return self._get(key, current.lchild)
        else:
            return self._get(key, current.rchild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self._delete(node_to_remove)
                self.size -= 1
        elif self.size == 1 and key == self.root.key:
            self.root = None
            self.size = 0
        else:
            raise KeyError("Error, key not in the tree!")

    def _delete(self, node):
        if node.is_leaf():
            if node == node.parent.lchild:
                node.parent.lchild = None
            else:
                node.parent.rchild = None
        elif node.has_both_children():
            succssor = node.find_succssor()
            succssor.splice_out()
            node.key = succssor.key
            node.value = succssor.value
        else:
            if node.has_left_child():
                if node.is_left_child():
                    node.lchild.parent = node.parent
                    node.parent.lchild = node.lchild
                elif node.is_right_child():
                    node.rchild.parent = node.parent
                    node.parent.rchild = node.rchild
                else:
                    node.replace_node(
                        node.lchild.key,
                        node.lchild.value,
                        node.lchild.lchild,
                        node.lchild.rchild
                    )
            else:
                if node.is_left_child():
                    node.rchild.parent = node.parent
                    node.parent.lchild = node.rchild
                elif node.is_right_child():
                    node.rchild.parent = node.parent
                    node.parent.rchild = node.rchild
                else:
                    node.replace_node(
                        node.rchild.key,
                        node.rchild.value,
                        node.rchild.lchild,
                        node.rchild.rchild
                    )

    def __delitem__(self, key):
        self.delete(key)


class AVL_Tree(BinSearchTree):
    def _put(self, key, value, current):
        if key < current.key:
            if current.has_left_child():
                self._put(key, value, current.lchild)
            else:
                current.lchild = TreeNode(key, value)
                self.update_balance(current.lchild)
        else:
            if current.has_right_child():
                self._put(key, value, current.rchild)
            else:
                current.rchild = TreeNode(key, value)
                self.update_balance(current.rchild)

    def update_balance(self, node):
        if node.balance > 1 or node.balance < -1:
            self.rebalance(node)
            return

        if node.parent is not None:
            if node.is_left_child():
                node.balance += 1
            else:
                node.balance -= 1

        if node.parent.balance != 0:
            self.update_balance(node.parent)

    def rebalance(self, node):
        if node.balance > 0:
            if node.lchild.balance < 0:
                self.rotate_left(node.lchild)
            self.rotate_right(node)
        elif node.balance < 0:
            if node.rchild.balance > 0:
                self.rotate_right(node.rchild)
            self.rotate_left(node)

    def rotate_left(self, old_root):
        new_root = old_root.rchild
        old_root.rchild = new_root.lchild
        if new_root.lchild is not None:
            new_root.lchild.parent = old_root
        new_root.parent = old_root.parent
        if old_root.is_root():
            self.root = new_root
        else:
            if old_root.is_left_child():
                old_root.parent.lchild = new_root
            else:
                old_root.parent.rchild = new_root

        new_root.lchild = old_root
        old_root.parent = new_root
        old_root.balance = old_root.balance - min(new_root.balance, 0) + 1
        new_root.balance = new_root.balance + max(old_root.balance, 0) + 1

    def rotate_right(self, old_root):
        new_root = old_root.lchild
        old_root.lchild = new_root.rchild
        if new_root.rchild is not None:
            new_root.rchild.parent = old_root
        new_root.parent = old_root.parent
        if old_root.is_root():
            self.root = new_root
        else:
            if old_root.is_left_child():
                old_root.parent.lchild = new_root
            else:
                old_root.parent.rchild = new_root

        new_root.rchild = old_root
        old_root.parent = new_root
        old_root.balance = old_root.balance - max(new_root.balance, 0) - 1
        new_root.balance = new_root.balance + min(old_root.balance, 0) - 1


class TreeNode:

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.lchild = left
        self.rchild = right
        self.parent = parent

    def __iter__(self):
        if self:
            if self.has_left_child():
                for item in self.lchild:
                    yield item
            yield self.key
            if self.has_right_child():
                for item in self.rchild:
                    yield item

    def has_left_child(self):
        return self.lchild

    def has_right_child(self):
        return self.rchild

    def is_left_child(self):
        return self.parent and self.parent.lchild == self

    def is_right_child(self):
        return self.parent and self.parent.rchild == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.lchild or self.rchild)

    def has_any_children(self):
        return self.lchild or self.rchild

    def has_both_children(self):
        return self.lchild and self.rchild

    def replace_node(self, new_key, new_val, new_lchild, new_rchild):
        self.key = new_key
        self.value = new_val
        self.lchild = new_lchild
        self.rchild = new_rchild
        if self.has_left_child():
            self.lchild.parent = self
        if self.has_right_child():
            self.rchild.parent = self

    def find_succssor(self):
        succssor = None
        if self.has_right_child():
            succssor = self.rchild.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succssor = self.parent
                else:
                    # 为什么该节点是右子树且无右孩子时，其继承人就是它的父节点的继承人？
                    self.parent.rchild = None
                    succssor = self.parent.find_succssor()
                    self.parent.rchild = self
        return succssor

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.lchild
        return current

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.lchild = None
            else:
                self.parent.rchild = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.lchild = self.lchild
                else:
                    self.parent.rchild = self.lchild
                self.lchild.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.lchild = self.rchild
                else:
                    self.parent.rchild = self.rchild
                self.rchild.parent = self.parent


if __name__ == '__main__':
    my_search_tree = BinSearchTree()
    my_search_tree['I'] = 'Plutors'
    my_search_tree['U'] = 'Coron'
    my_search_tree['she'] = 'Bea'
    print(my_search_tree['I'])
    print(my_search_tree['U'])
    del my_search_tree['she']
    print(my_search_tree['she'])
