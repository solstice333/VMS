from pm import *

INPUT_PATH = "resources/"
INPUT_FILE = "pm.txt"
INPUT_FILE_2 = "input2.txt"


class CPU:
    def __init__(self, outfile):
        self._outfile = outfile
        self._pm = PM(INPUT_PATH + INPUT_FILE)
        self._pairs_of_virtual_addresses = Parser(INPUT_PATH + INPUT_FILE_2)


    def convert_va_to_pa(self, tlb):
        if tlb:
            pass
        else:
            for wr, va in self._pairs_of_virtual_addresses.get_pairs():
                s, p, w = self._split_virtual_address(va)
                if wr == 1:  # Write only
                    self._write(s, p, w)
                else:  # Ready only
                    self._read(s, p, w)

    def _write(self, s, p, w):
        seg_entry = self._pm[s]
        if self._eval_addr_for_wr(seg_entry, 1):
            pt_entry = self._pm[self._pm[s] + p]
            if self._eval_addr_for_wr(pt_entry, 2):
                page_entry = pt_entry + w
                self._outfile.write(str(page_entry) + ' ')

    def _read(self, s, p, w):
        seg_entry = self._pm[s]
        if self._eval_addr_for_rd(seg_entry):
            pt_entry = self._pm[self._pm[s] + p]
            if self._eval_addr_for_rd(pt_entry):
                page_entry = pt_entry + w
                self._outfile.write(str(page_entry) + ' ')

    def _split_virtual_address(self, decimal_value):
        bin_to_dec = lambda bin_num : int(bin_num, 2)
        binary_number = "{0:028b}".format(decimal_value)
        s_bin = binary_number[:9]
        p_bin = binary_number[9:19]
        w_bin = binary_number[19:]
        return bin_to_dec(s_bin), bin_to_dec(p_bin), bin_to_dec(w_bin)


    def _eval_addr_for_rd(self, num):
        if num == -1:
            self._outfile.write('pf ')
        elif num == 0:
            self._outfile.write('err ')
        else:
            return True
        return False


    def _eval_addr_for_wr(self, num, one_or_two_bits):
        if num == -1:
            self._outfile.write('pf ')
            return False
        elif num == 0:
            if one_or_two_bits == 1:
                self._pm.set_next_empty_bit()
            else:
                self._pm.set_next_empty_pair_bits()
        return True
