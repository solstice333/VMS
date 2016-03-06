from exceptions import TooDamnMuchDammitError


# Bitmap : class for creating and interfacing with bitmaps
class Bitmap:
    MAX = 2 ** 1024 - 1
    MAX_BIT = 1023

    # Bitmap(init_val = 0) : Bitmap constructor. |init_val| is defaulted
    # to 0. |init_val| represents the initial value of the Bitmap. |init_val|
    # cannot be more than 2**1024 - 1 otherwise an exception is raised
    def __init__(self, init_val=0):
        if init_val > self.MAX:
            raise TooDamnMuchDammitError
        self._fatass = init_val

    # get_bitmap_as_indices() : returns the mapped indices as an array where
    # each value in the array represents the bit that has been set. The indices
    # are zero-based. For example, if a value 1 was in the array, that means
    # bit 1 has been set. Likewise, if a value of 0 was in the array, that means
    # bit 0 has been set.
    def get_bitmap_as_indices(self):
        fatass_copy = self._fatass
        damnbits = []

        for i in range(1024):
            if fatass_copy & 1:
                damnbits.append(i)
            fatass_copy >>= 1

        return damnbits

    # set_bit(bitnum) : sets bit number |bitnum|. |bitnum| is zero based.
    def set_bit(self, bitnum):
        if bitnum > self.MAX_BIT:
            raise TooDamnMuchDammitError
        self._fatass |= 1 << bitnum

    # clr_bit(bitnum) : clears bit number |bitnum|. |bitnum| is zero based.
    def clr_bit(self, bitnum):
        if bitnum > self.MAX_BIT:
            raise TooDamnMuchDammitError
        self._fatass &= ~(1 << bitnum)

    # is_bit_set(bitnum) : checks if bit number |bitnum| is set to 1. |bitnum|
    # is zero based. Returns True if set. False otherwise.
    def is_bit_set(self, bitnum):
        if bitnum > self.MAX_BIT:
            raise TooDamnMuchDammitError
        return bool(self._fatass & 1 << bitnum)

    # find_next_empty_bit() : returns the zero based bit number of the 
    # beginning block of bits that have not been set. |numbits| is the
    # number of bits required to be free. For example, if |numbits| was 2
    # and the returned value was 10, then bit 10 and bit 11 are unset.
    def get_next_empty_bits(self, numbits):
        if numbits <= 0:
            return -1

        for i in range(Bitmap.MAX_BIT + 1):
            nextbit = False

            for j in range(numbits):
                if i + j > Bitmap.MAX_BIT:
                    return -1
                if self.is_bit_set(i + j):
                    nextbit = True
                    break

            if nextbit:
                continue
            return i

        return -1

    # __str__(): string representation of a Bitmap instance is its hex
    # value
    def __str__(self):
        return hex(self._fatass)
