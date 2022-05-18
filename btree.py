# """
# Binary tree for building the game tree
# """

class LinkedBinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        t = LinkedBinaryTree(new_node)
        if self.left_child == None:
            self.left_child = t
        else:
            t.left_child = self.left_child
            self.left_child = t
        return t

    def insert_right(self, new_node):
        t = LinkedBinaryTree(new_node)
        if self.right_child == None:
            self.right_child = t
        else:
            t.right_child = self.right_child
            self.right_child = t
        return t

    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""

        def recurse(node, level):
            # print(node.right_child)
            s = ""
            if node is not None:
                s += recurse(node.right_child, level + 1)
                s += "| " * level
                s += str(node.key) + "\n"
                s += recurse(node.left_child, level + 1)
            return s
        return recurse(self, 0)

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.key)
        if self.right_child:
            self.right_child.inorder()

    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.key)
