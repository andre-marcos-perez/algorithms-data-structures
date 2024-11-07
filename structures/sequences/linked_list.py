from typing import Union

from structures.sequence import Sequence, T


class LinkedListNode:

    def __init__(self, x: T) -> None:
        self.item: T = x
        self.next: Union[LinkedListNode, None] = None

    def get(self, i: int):
        return self if i == 0 else self.next.get(i - 1)


class LinkedList(Sequence):

    def __init__(self):
        self.head: Union[LinkedListNode, None] = None
        self.size: int = 0

    def __len__(self):  # O(1)
        return self.size

    def __iter__(self):  # O(n)
        node = self.head
        while node:
            yield node.item
            node = node.next

    def get(self, i: int) -> T:  # O(i)
        node = self.head.get(i)
        return node.item

    def set(self, i: int, x: T) -> None:  # O(i)
        node = self.head.get(i)
        node.item = x

    def insert(self, i: int, x: T) -> None:  # O(i)
        if i == 0:
            self.insert_first(x)
        node = LinkedListNode(x)
        prev_node = self.get(i - 1)
        node.next = prev_node.next
        prev_node.next = node
        self.size += 1

    def delete(self, i: int) -> T:  # O(i)
        if i == 0:
            return self.delete_first()
        prev_node = self.get(i - 1)
        item = prev_node.next.item
        prev_node.next = prev_node.next.next
        self.size -= 1
        return item

    def insert_first(self, x: T) -> None:  # O(1)
        node = LinkedListNode(x)
        node.next = self.head
        self.head = node
        self.size += 1

    def delete_first(self) -> T:  # O(1)
        item = self.head.item
        self.head = self.head.next
        self.size -= 1
        return item

    def insert_last(self, item: T) -> None:  # O(n)
        self.insert(self.size, item)

    def delete_last(self) -> T:  # O(n)
        return self.delete(self.size - 1)
