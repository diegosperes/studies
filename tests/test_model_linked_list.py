from unittest import TestCase

from models.linked_list import LinkedList

class LinkedListModel(TestCase):

    def setUp(self):
        self.linked_list = LinkedList('A')

    def test_get_value(self):
        self.assertEqual('A', self.linked_list.value)

    def test_add_node(self):
        self.linked_list.add('B')
        self.assertEqual('B', self.linked_list.next.value)

    def test_get_end_node(self):
        self.linked_list.add('B')
        self.linked_list.add('C')
        self.assertEqual('C', self.linked_list.end.value)

    def test_iterable_protocol(self):
        self.linked_list.add('B')
        self.linked_list.add('C')
        nodes = [node for node in self.linked_list]
        
        self.assertEqual(3, len(nodes))
        self.assertEqual('A', nodes[0].value)
        self.assertEqual('B', nodes[1].value)
        self.assertEqual('C', nodes[2].value)
