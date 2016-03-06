from inputparser import *
from frame import *
from bitmap import *
from exceptions import *


class PM:
    SIZE = 1024

    def __init__(self, file_name):
        self._frames = [Frame() for i in range(PM.SIZE)]
        self._parser = Parser(file_name)
        self._seg_table = self._frames[0]
        self._bitmap = Bitmap()
        self._bitmap.set_bit(0)  # Segment table occupies the first bit of the bitmap.
        self._init_seg_table()
        self._init_page_table()

    @staticmethod
    def get_index_from_words(words):
        return words // Frame.get_size()

    def get_bitmap(self):
        return str(self._bitmap)

    def __getitem__(self, idx):
        if type(idx) is not int:
            raise IsNotNumericalValue

        if idx < 0 or idx >= PM.SIZE * Frame.SIZE:
            raise IndexError("PM index out of range")

        return self._frames[idx // Frame.SIZE][idx % Frame.SIZE]

    def __setitem__(self, key, value):
        if type(key) is not int or type(value) is not int:
            raise IsNotNumericalValue

        if key < 0 or key >= PM.SIZE * Frame.SIZE:
            raise IndexError("PM index out of range")

        if value > 2**32 - 1:
            raise ValueTooLarge

        self._frames[key // Frame.SIZE][key % Frame.SIZE] = value

    def set_next_empty_bit(self):
        i = self._bitmap.find_next_empty_bit()
        self._bitmap.set_bit(i)

    def set_next_empty_pair_bits(self):
        i = self._bitmap.find_next_empty_pair_bits()
        self._bitmap.set_bit(i)
        self._bitmap.set_bit(i+1)

    def _init_seg_table(self):
        for s, address_of_page_table in self._parser.get_pairs():
            self._seg_table[s] = address_of_page_table

            if address_of_page_table != -1:
                idx = PM.get_index_from_words(address_of_page_table)
                self._bitmap.set_bit(idx)
                self._bitmap.set_bit(idx + 1)

    def _init_page_table(self):
        for p, s, address_of_page in self._parser.get_triples():
            address_of_page_table = self._seg_table[s]

            if address_of_page_table != -1:
                idx = PM.get_index_from_words(address_of_page_table) # self._seg_table[s] should always be a power of 2...

                self._frames[idx][p] = address_of_page
                if address_of_page != -1:
                    self._bitmap.set_bit(PM.get_index_from_words(address_of_page))
