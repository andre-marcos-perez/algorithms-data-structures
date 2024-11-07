from abc import ABC, abstractmethod
from typing import TypeVar, Union

T = TypeVar("T")
K = TypeVar("K")


class Set(ABC):

    # -- Static operations

    @abstractmethod
    def find(self, k: K) -> Union[T, None]:
        """Return a stored item x with key k or None if not found"""
        raise NotImplementedError()

    # -- Dynamic operations

    @abstractmethod
    def insert(self, x: T) -> None:
        """Insert a new item x with key k"""
        raise NotImplementedError()

    @abstractmethod
    def delete(self, k: T) -> T:
        """Delete and return a stored item x with key x"""
        raise NotImplementedError()

    # -- Order operations

    @abstractmethod
    def __iter__(self):
        """Return items one by one in key order"""
        raise NotImplementedError()

    @abstractmethod
    def min(self) -> T:
        """Return a stored item with the smallest key k"""
        raise NotImplementedError()

    @abstractmethod
    def max(self) -> T:
        """Return a stored item with the largest key k"""
        raise NotImplementedError()

    def next(self, k: K) -> T:
        """Return a stored item with the smallest key larger than k"""
        raise NotImplementedError()

    @abstractmethod
    def prev(self, k: K) -> T:
        """Return a stored item with the largest key smaller than k"""
        raise NotImplementedError()
