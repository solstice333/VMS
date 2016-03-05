from kyleParser import *
from frame import *
from bitmap import *


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
