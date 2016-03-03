from exceptions import *


class Frame:
    def __init__(self, size=512):
        self._size = size
        self._words = [0] * size

    def __getitem__(self, item):
        if type(item) is not int:
            raise IsNotNumericalValue

        if item < 0 or item >= self._size:
            raise IndexingError

        return self._words[item]

    def __setitem__(self, key, value):
        if type(key) is not int or type(value) is not int:
            raise IsNotNumericalValue

        if key < 0 or key >= self._size:
            raise IndexingError

        if value > 2**32 - 1:
            raise ValueTooLarge

        self._words[key] = value

    def __repr__(self):
        return str(self._words)


if __name__ == '__main__':
    f = Frame(10)
    f[0] = 2
    print(f)
