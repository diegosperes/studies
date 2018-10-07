

class LinkedList:

    @property
    def end(self):
        return [node for node in self][-1]

    def __init__(self, value):
        self.value = value
        self.next = None
        self._tmp = self

    def add(self, value):
        self.end.next = LinkedList(value)

    def __iter__(self):
        return self

    def __next__(self):
        if not self._tmp:
            self._tmp = self
            raise StopIteration()

        node = self._tmp
        self._tmp = node.next
        return node
