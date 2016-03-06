from exceptions import *


class Buffer:
    MAX_LRU_VALUE = 3

    def __init__(self):
        self._lru_value = 0
        self._sp = -1
        self._f = -1

    def get_lru_value(self):
        return self._lru_value

    def get_sp(self):
        return self._sp

    def get_f(self):
        return self._f

    def decrement_lru_value(self):
        if self._lru_value != 0:
            self._lru_value -= 1

    def max_lru_value(self):
        self._lru_value = Buffer.MAX_LRU_VALUE

    def set_sp(self, sp):
        if type(sp) is not str:
            raise IsNotStringValue
        self._sp = int(sp, 2)

    def set_f(self, pt_entry):
        self._f = pt_entry  # which holds the address to the page


class TLB:
    SIZE = 4

    def __init__(self, physical_memory, outfile):
        self._pm = physical_memory
        self._outfile = outfile
        self._buffers = [Buffer() for i in range(TLB.SIZE)]

    def get_f(self, idx):
        return self._buffers[idx].get_f()

    def find_matching_buffer(self, sp):
        for i in range(TLB.SIZE):
            # print(i, self._buffers[i].get_lru_value(), self._buffers[i].get_sp(), self._buffers[i].get_f())
            if self._buffers[i].get_sp() == int(sp, 2):
                self._outfile.write('h ')
                # print()
                return i
        # print()
        self._outfile.write('m ')
        return -1

    def update_matching_buffer(self, idx):
        self._buffers[idx].max_lru_value()
        self._decrement_all_lru_except_idx(idx)

    def replace_old_buffer(self, sp):
        idx = self._find_old_buffer_idx()
        s = int(sp[:9], 2)
        p = int(sp[9:], 2)

        pm = self._pm
        self._buffers[idx].max_lru_value()
        self._buffers[idx].set_sp(sp)
        self._buffers[idx].set_f(pm[pm[s] + p])
        self._decrement_all_lru_except_idx(idx)

    def _decrement_all_lru_except_idx(self, idx):
        for i in range(TLB.SIZE):
            if idx == i:
                continue
            self._buffers[i].decrement_lru_value()

    def _find_old_buffer_idx(self):
        for i in range(TLB.SIZE):
            if self._buffers[i].get_lru_value() == 0:
                return i
