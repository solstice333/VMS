from kyleParser import *
from frame import *
from bitmap import *


class PM:
    size = 1024

    def __init__(self, file_name):
        self._frames = [Frame() for i in range(PM.size)]
        self._parser = Parser(file_name)
        self._seg_table = self._frames[0]
        self._bitmap = Bitmap()
        self._bitmap.set_bit(0) # Segment table occupies the first bit of the bitmap.

        for s, f in self._parser.get_pairs():
            self._seg_table[s] = f

            address_of_page_table = self._seg_table[s]
            if address_of_page_table != -1:
                idx = PM.get_index(address_of_page_table)
                self._bitmap.set_bit(idx)
                self._bitmap.set_bit(idx + 1)

        for p, s, f in self._parser.get_triples():
            address_of_page_table = self._seg_table[s]
            if address_of_page_table != -1:
                idx = PM.get_index(address_of_page_table) # self._seg_table[s] should always be a power of 2...
                self._frames[idx][p] = f
                if f != -1:
                    self._bitmap.set_bit(PM.get_index(f))

        print(self._bitmap)

    @staticmethod
    def get_index(words):
        return words // Frame.get_size()
