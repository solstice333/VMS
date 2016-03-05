from exceptions import *


class Frame:
    SIZE = 512

    def __init__(self):
        self._words = [0] * Frame.SIZE

    def __getitem__(self, item):
        if type(item) is not int:
            raise IsNotNumericalValue

        if item < 0 or item >= Frame.SIZE:
            raise IndexError

        return self._words[item]

    def __setitem__(self, key, value):
        if type(key) is not int or type(value) is not int:
            raise IsNotNumericalValue

        if key < 0 or key >= Frame.SIZE:
            raise IndexError("Frame index out of range")

        if value > 2**32 - 1:
            raise ValueTooLarge

        self._words[key] = value

    def __repr__(self):
        return str(self._words) + "\n"

    @classmethod
    def get_size(cls):
        return cls.SIZE
