class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Adding that many cookies would exceed the jar's capacity")
        else:
            self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw a negative amount")
        elif self._size < n:
            raise ValueError("Not enough cookies in the jar")
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0 or not isinstance(capacity, int):
            raise ValueError("Capacity must be greater than 0 and an integer")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0 or not isinstance(size, int):
            raise ValueError("Size must be greater than 0 and an integer")
        if size > self._capacity:
            self._size = self._capacity
        else:
            self._size = size

