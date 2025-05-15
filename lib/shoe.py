#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self._condition = "New"

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self._brand = value
        else:
            raise ValueError("Brand must be a string")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        if isinstance(value, str):
            self._condition = value
        else:
            raise ValueError("Condition must be a string")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
