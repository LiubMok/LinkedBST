class BTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left_child = left
        self.right_child = right

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def insert_left(self, value):
        self.left_child = value

    def insert_right(self, value):
        self.right_child = value

    def is_leaf(self):
        return self.left_child is None and self.right_child is None

