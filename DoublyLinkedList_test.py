import unittest
from DoublyLinkedList import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.lst = DoublyLinkedList()

    def test_append(self):
        self.lst.append('A')
        self.lst.append('B')
        self.assertEqual(self.lst.length(), 2)
        self.assertEqual(self.lst.get(0), 'A')
        self.assertEqual(self.lst.get(1), 'B')

    def test_insert(self):
        self.lst.insert('A', 0)
        self.lst.insert('B', 1)
        self.lst.insert('C', 1)  # вставка в середину
        self.assertEqual([self.lst.get(i) for i in range(self.lst.length())], ['A', 'C', 'B'])

    def test_delete(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('C')
        deleted = self.lst.delete(1)
        self.assertEqual(deleted, 'B')
        self.assertEqual([self.lst.get(i) for i in range(self.lst.length())], ['A', 'C'])

    def test_delete_all(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('A')
        self.lst.deleteAll('A')
        self.assertEqual([self.lst.get(i) for i in range(self.lst.length())], ['B'])

    def test_find_first_last(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('A')
        self.assertEqual(self.lst.findFirst('A'), 0)
        self.assertEqual(self.lst.findLast('A'), 2)

    def test_clone(self):
        self.lst.append('A')
        self.lst.append('B')
        cloned = self.lst.clone()
        self.assertEqual([cloned.get(i) for i in range(cloned.length())], ['A', 'B'])

    def test_reverse(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('C')
        self.lst.reverse()
        self.assertEqual([self.lst.get(i) for i in range(self.lst.length())], ['C', 'B', 'A'])

    def test_extend(self):
        other = DoublyLinkedList()
        other.append('X')
        other.append('Y')
        self.lst.append('A')
        self.lst.extend(other)
        self.assertEqual([self.lst.get(i) for i in range(self.lst.length())], ['A', 'X', 'Y'])

    def test_clear(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.clear()
        self.assertEqual(self.lst.length(), 0)

    def test_failing_example(self):
        self.assertEqual(1, 2)


if __name__ == '__main__':
    unittest.main()