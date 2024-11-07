import unittest

from structures.sequences.linked_list import LinkedList


class TestContainer(unittest.TestCase):

    def setUp(self):
        self.collection = (1, 2, 3)
        self.struct = LinkedList()
        self.struct.build(self.collection)

    def test_len(self):
        self.assertEqual(len(self.struct), len(self.collection))

    def test_build(self):
        for i, item in enumerate(self.struct):
            self.assertEqual(item, self.collection[i])


class TestStaticOperations(unittest.TestCase):

    def setUp(self):
        self.collection = (1, 2, 3)
        self.struct = LinkedList()
        self.struct.build(self.collection)

    def test_get(self):
        item = self.struct.get(2)
        self.assertEqual(item, 3)

    def test_set(self):
        self.struct.set(2, 9)
        item = self.struct.get(2)
        self.assertEqual(item, 9)


class TestDynamicOperations(unittest.TestCase):

    def setUp(self):
        self.collection = (1, 2, 3)
        self.struct = LinkedList()
        self.struct.build(self.collection)

    def test_insert_first(self):
        self.struct.insert_first(9)
        item = self.struct.get(0)
        self.assertEqual(item, 9)

    def test_delete_first(self):
        item = self.struct.get(0)
        deleted = self.struct.delete_first()
        self.assertEqual(deleted, item)

    def test_insert_last(self):
        self.struct.insert_last(7)
        item = self.struct.get(len(self.struct) - 1)
        self.assertEqual(item, 7)

    def test_delete_last(self):
        item = self.struct.get(len(self.struct) - 1)
        deleted = self.struct.delete_last()
        self.assertEqual(deleted, item)

    def test_insert(self):
        self.struct.insert(1, 9)
        # prev
        item = self.struct.get(0)
        self.assertEqual(item, 1)
        # current
        item = self.struct.get(1)
        self.assertEqual(item, 9)
        # next
        item = self.struct.get(2)
        self.assertEqual(item, 2)

    def test_delete(self):
        item = self.struct.delete(1)
        self.assertEqual(item, 2)
        # prev
        item = self.struct.get(0)
        self.assertEqual(item, 1)
        # current
        item = self.struct.get(1)
        self.assertEqual(item, 3)


if __name__ == "__main__":
    unittest.main()
