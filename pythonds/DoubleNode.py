class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.back = None
        self.next = None

    def get_data(self):
        return self.data

    def get_back(self):
        return self.back

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_back(self, new_back):
        self.back = new_back

    def set_next(self, new_next):
        self.next = new_next
