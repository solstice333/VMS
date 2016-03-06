from pm import *


class CPU:
    def __init__(self, outfile, initfile, vafile):
        self._outfile = open(outfile, "w")
        self._pm = PM(initfile)
        self._pairs_of_virtual_addresses = Parser(vafile)

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
        if not self._eval_addr_for_wr(s, True):
            self._eval_addr_for_wr(self._pm[s] + p, False)
        else:
            entry = self._pm[self._pm[self._pm[s] + p] + w]
            self._outfile.write(str(entry) + ' ')

    # TODO
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

    def _eval_addr_for_wr(self, idx, is_page_table):
        addr = self._pm[idx]

        if addr == -1:
            self._outfile.write('pf ')
        elif addr == 0:
            if is_page_table:
                self._pm.fralloc(idx, 2)
            else:
                self._pm.fralloc(idx, 1)

        return addr
