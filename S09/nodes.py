class Node:

    def __init__(self, name:int, parent=None):
        self.name = name
        self.children = []
        if parent is not None:
            self.parent = Node(parent)
            self.parent.children.append(self)

    @property
    def has_no_children(self):
        return

    @property
    def has_no_parent(self):
        return self.parent is None

    def chain(self):
        if self.has_no_parent:
            return [self]
        else:
            return self.parent.chain() + [self]

