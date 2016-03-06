from exceptions import TooDamnMuchDammitError


# Bitmap : class for creating and interfacing with bitmaps
class Bitmap:
    MAX = 2 ** 1024 - 1
    MAX_BIT = 1023

    # Bitmap(init_val = 0) : Bitmap constructor. |init_val| is defaulted
    # to 0. |init_val| represents the initial value of the Bitmap. |init_val|
    # cannot be more than 2**1024 - 1 otherwise an exception is raised
    def __init__(self, init_val=0):
        #if init_val > self.MAX:
        #    raise TooDamnMuchDammitError
        #self._fatass = init_val
        self._bitmap = [0 for i in range(1024)]

    # get_bitmap_as_indices() : returns the mapped indices as an array where
    # each value in the array represents the bit that has been set. The indices
    # are zero-based. For example, if a value 1 was in the array, that means
    # bit 1 has been set. Likewise, if a value of 0 was in the array, that means
    # bit 0 has been set.
    def get_bitmap_as_indices(self):
        #fatass_copy = self._fatass
        #damnbits = []

        #for i in range(1024):
        #    if fatass_copy & 1:
        #        damnbits.append(i)
        #    fatass_copy >>= 1

        #return damnbits
        pass

    # set_bit(bitnum) : sets bit number |bitnum|. |bitnum| is zero based.
    def set_bit(self, bitnum):
        #if bitnum > self.MAX_BIT:
        #    raise TooDamnMuchDammitError
        #self._fatass |= 1 << bitnum
        self._bitmap[bitnum] = 1

    # clr_bit(bitnum) : clears bit number |bitnum|. |bitnum| is zero based.
    def clr_bit(self, bitnum):
        #if bitnum > self.MAX_BIT:
        #    raise TooDamnMuchDammitError
        #self._fatass &= ~(1 << bitnum)
        self._bitmap[bitnum] = 0

    # is_bit_set(bitnum) : checks if bit number |bitnum| is set to 1. |bitnum|
    # is zero based. Returns True if set. False otherwise.
    def is_bit_set(self, bitnum):
        #if bitnum > self.MAX_BIT:
        #    raise TooDamnMuchDammitError
        #return bool(self._fatass & 1 << bitnum)
        return self._bitmap[bitnum] == 1

    def find_next_empty_bit(self):
        for i in range(1024):
            if self._bitmap[i] == 0:
                return i
        return -1

    def find_next_empty_bits(self):
        for i in range(1023):
            if self._bitmap[i] == 0 and self._bitmap[i+1] == 0:
                return i
        return -1

    # __str__(): string representation of a Bitmap instance is its hex
    # value
    def __str__(self):
        #return hex(self._fatass)
        pass
