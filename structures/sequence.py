from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T")


class Sequence(ABC):

    # -- Static operations

    @abstractmethod
    def __iter__(self):
        """Return items one by one in sequence order"""
        raise NotImplementedError()

    @abstractmethod
    def get(self, i: int) -> T:
        """Return a stored item at index i"""
        raise NotImplementedError()

    @abstractmethod
    def set(self, i: int, x: T) -> None:
        """Set a new item x at index i"""
        raise NotImplementedError()

    # -- Dynamic operations

    @abstractmethod
    def insert(self, i: int, x: T) -> None:
        """Insert a new item x at index i"""
        raise NotImplementedError()

    @abstractmethod
    def delete(self, i: int) -> T:
        """Delete and return a stored item x at index i"""
        raise NotImplementedError()

    @abstractmethod
    def insert_first(self, x: T) -> None:
        """Insert a new item x at index i=0"""
        raise NotImplementedError()

    @abstractmethod
    def delete_first(self) -> T:
        """Delete and return a stored item x at index i=0"""
        raise NotImplementedError()

    @abstractmethod
    def insert_last(self, item: T) -> None:
        """Insert a new item x at index i=len(sequence)-1"""
        raise NotImplementedError()

    @abstractmethod
    def delete_last(self) -> T:
        """Delete and return a stored item x at index i=len(sequence)-1"""
        raise NotImplementedError()
